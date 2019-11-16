from pyspark import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode,posexplode,split
from core.api import *
from core.s3_integration import *
import json #packge to handle json files
import os


def getSparkConf():

    sparkConfiguration = SparkConf().setAppName('Brazilian Leagues Information').setMaster('local') #set application configuration
    sparkContext = SparkContext(conf=sparkConfiguration) #Set cluster information
    sparkSession =  SparkSession(sparkContext)\
        .builder\
        .appName('Brazilian Leagues Information')\
        .getOrCreate()
    #set a session which allows user to write HiveQL

    return sparkConfiguration, sparkContext, sparkSession

def uploadJsonBrazilLeagues(season=''):

    complementFileName = ''
    if not(season == ''):
        complementFileName = '_' + str(season)

    jsonFileName = 'brazilian_league' + complementFileName + '.json'

    if not(file_exists(jsonFileName)):
        footballApi = FootballApi()
        jsonRawData = footballApi.leagues('brazil', season).json()
        brLeague = json.dumps(jsonRawData)
        with open(jsonFileName, 'w') as file:
            json.dump(brLeague, file)

        upload_file(jsonFileName)
        print('Json file has been uploaded to S3.')
        #os.remove(jsonFileName)
        print('Json file has been removed locally.')

    return jsonFileName


def getBrazilianLeagues(season=''):

    #get the spark configuration, context and session
    sparkConfiguration, sparkContext, sparkSession = getSparkConf()

    #invokes the api to get the json file with brazilian league data,
    #upload the file to AWS s3 and return the file name
    fileName = uploadJsonBrazilLeagues(season)

    #get the data from the file hosted in S3
    #json.loads parse the json we've got from S3 into a dictonary
    fileData = json.loads(load_file(fileName))

    #Creates a RDD which allows data to be operated on in parallel
    rddDataFrame = sparkContext.parallelize([fileData])

    #create a data frame in SQL Session which allows this data fram being manipulated with sql commands
    dataFrame = sparkSession.read.json(rddDataFrame)

    #print the json schema
    dataFrame.printSchema()
    #root
    #|-- api: struct (nullable = true)
    #|    |-- leagues: array (nullable = true)
    #|    |    |-- element: struct (containsNull = true)
    #|    |    |    |-- country: string (nullable = true)
    #|    |    |    |-- country_code: string (nullable = true)
    #|    |    |    |-- coverage: struct (nullable = true)
    #|    |    |    |    |-- fixtures: struct (nullable = true)
    #|    |    |    |    |    |-- events: boolean (nullable = true)
    #|    |    |    |    |    |-- lineups: boolean (nullable = true)
    #|    |    |    |    |    |-- players_statistics: boolean (nullable = true)
    #|    |    |    |    |    |-- statistics: boolean (nullable = true)
    #|    |    |    |    |-- odds: boolean (nullable = true)
    #|    |    |    |    |-- players: boolean (nullable = true)
    #|    |    |    |    |-- predictions: boolean (nullable = true)
    #|    |    |    |    |-- standings: boolean (nullable = true)
    #|    |    |    |    |-- topScorers: boolean (nullable = true)
    #|    |    |    |-- flag: string (nullable = true)
    #|    |    |    |-- is_current: long (nullable = true)
    #|    |    |    |-- league_id: long (nullable = true)
    #|    |    |    |-- logo: string (nullable = true)
    #|    |    |    |-- name: string (nullable = true)
    #|    |    |    |-- season: long (nullable = true)
    #|    |    |    |-- season_end: string (nullable = true)
    #|    |    |    |-- season_start: string (nullable = true)
    #|    |    |    |-- standings: long (nullable = true)
    #|    |    |    |-- type: string (nullable = true)
    #|    |-- results: long (nullable = true)

    # the below command I can use to show the content of the dataFrame
    # but the first level is API, so the outcome is all the json file
    dataFrame.show()
    #+--------------------+
    #|                 api|
    #+--------------------+
    #|[[[Brazil, BR, [[...|
    #+--------------------+

    #The command below will show the value of results column
    dataFrame.select(dataFrame['api']['results']).show()
    #+-----------+
    #|api.results|
    #+-----------+
    #|         33|
    #+-----------+

    dataFrame.select('api.results').show()
    #+-------+
    #|results|
    #+-------+
    #|     33|
    #+-------+

    #the below command allow you to create a view and then execute sql statemants
    dataFrame.createOrReplaceTempView('vw_brazilian_leagues')

    #Simple query to bring the data with posexplode which is transposing each row
    dataFrameView = sparkSession.sql("""
    select names.id_championship,
           names.championship,
           seasons.id_season,
           seasons.season,
           types.id_type,
           types.type
    from vw_brazilian_leagues l LATERAL VIEW posexplode(l.api.leagues.name) names as id_championship, championship
                                LATERAL VIEW posexplode(l.api.leagues.season) seasons as id_season, season
                                LATERAL VIEW posexplode(l.api.leagues.type) types as id_type, type
    where id_championship == id_season and id_championship = id_type
    """)
    dataFrameView.show(35)
    #+---------------+----------------+---------+------+-------+------+
    #|id_championship|    championship|id_season|season|id_type|  type|
    #+---------------+----------------+---------+------+-------+------+
    #|              0|         Serie A|        0|  2018|      0|League|
    #|              1|         Serie B|        1|  2018|      1|League|
    #|              2|         Serie A|        2|  2017|      2|League|
    #|              3|         Serie B|        3|  2017|      3|League|
    #|              4|         Serie A|        4|  2016|      4|League|
    #|              5|         Serie B|        5|  2016|      5|League|
    #|              6|  Copa Do Brasil|        6|  2018|      6|   Cup|
    #|              7|  Copa Do Brasil|        7|  2017|      7|   Cup|
    #|              8|  Copa Do Brasil|        8|  2016|      8|   Cup|
    #|              9|Brasileiro Women|        9|  2016|      9|League|
    #|             10|Brasileiro Women|       10|  2017|     10|League|
    #|             11|Brasileiro Women|       11|  2018|     11|League|
    #|             12|  Copa Do Brasil|       12|  2019|     12|   Cup|
    #|             13|         Serie A|       13|  2019|     13|League|
    #|             14|         Serie B|       14|  2019|     14|League|
    #|             15|Brasileiro Women|       15|  2019|     15|League|
    #|             16|         Serie A|       16|  2015|     16|League|
    #|             17|         Serie A|       17|  2014|     17|League|
    #|             18|         Serie A|       18|  2013|     18|League|
    #|             19|         Serie A|       19|  2012|     19|League|
    #|             20|         Serie A|       20|  2011|     20|League|
    #|             21|         Serie A|       21|  2010|     21|League|
    #|             22|         Serie C|       22|  2019|     22|League|
    #|             23|         Serie C|       23|  2018|     23|League|
    #|             24|         Serie C|       24|  2017|     24|League|
    #|             25|         Serie C|       25|  2016|     25|League|
    #|             26|         Serie D|       26|  2019|     26|League|
    #|             27|         Serie D|       27|  2018|     27|League|
    #|             28|         Serie D|       28|  2017|     28|League|
    #|             29|         Serie D|       29|  2016|     29|League|
    #|             30|        Alagoano|       30|  2019|     30|   Cup|
    #|             31|        Alagoano|       31|  2018|     31|   Cup|
    #|             32|        Alagoano|       32|  2017|     32|   Cup|
    #+---------------+----------------+---------+------+-------+------+

    #Group by and Order by
    dataFrameViewGroupBy = sparkSession.sql("""
    select names.championship,
           types.type,
           count(*)
    from vw_brazilian_leagues l LATERAL VIEW posexplode(l.api.leagues.name) names as id_championship, championship
                                LATERAL VIEW posexplode(l.api.leagues.season) seasons as id_season, season
                                LATERAL VIEW posexplode(l.api.leagues.type) types as id_type, type
    where id_championship == id_season and id_championship = id_type
    Group By names.championship, types.type
    Order By types.type
    """)
    dataFrameViewGroupBy.show(35)
    #+----------------+------+--------+
    #|    championship|  type|count(1)|
    #+----------------+------+--------+
    #|  Copa Do Brasil|   Cup|       4|
    #|        Alagoano|   Cup|       3|
    #|         Serie B|League|       4|
    #|Brasileiro Women|League|       4|
    #|         Serie A|League|      10|
    #|         Serie D|League|       4|
    #|         Serie C|League|       4|
    #+----------------+------+--------+

    #Compare how was to transform the data with SQL commans to pyspark functions
    #explode the dataset
    dfChampionship = dataFrame.select(posexplode('api.leagues.name').alias('id', 'championship'))
    dfSeason = dataFrame.select(posexplode('api.leagues.season').alias('id', 'season'))
    dfType = dataFrame.select(posexplode('api.leagues.type').alias('id', 'type'))

    #set alias for each table
    ch = dfChampionship.alias('ch')
    ss = dfSeason.alias('ss')
    tp = dfType.alias('tp')

    ch.join(ss, ch.id == ss.id).join(tp, ch.id == tp.id).groupby('championship', 'type').count().orderBy('type').show()

    #+----------------+------+-----+
    #|    championship|  type|count|
    #+----------------+------+-----+
    #|  Copa Do Brasil|   Cup|    4|
    #|        Alagoano|   Cup|    3|
    #|         Serie B|League|    4|
    #|Brasileiro Women|League|    4|
    #|         Serie A|League|   10|
    #|         Serie D|League|    4|
    #|         Serie C|League|    4|
    #+----------------+------+-----+


    #Stop the sql session and you are no longer able to execute queries
    sparkSession.stop()
