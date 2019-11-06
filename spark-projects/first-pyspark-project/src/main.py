from core.config import Config
import requests # package to manipulate api
import rootpath # package to identify the root directory
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext
import json
from brazil_league.brazil_league_queries import get_brazilian_leagues


path = rootpath.detect()
config_file = Config(path+"/spark-projects/first-pyspark-project/src/config.yml")

headers = {
    'x-rapidapi-host': config_file.x_rapidapi_host,
    'x-rapidapi-key': config_file.x_rapidapi_key
    }

response = requests.request("GET", config_file.url_rapidapi, headers=headers)

sc = SparkContext('local')
spark =  SparkSession(sc)\
    .builder\
    .appName('Python Spark to analyse Brazilian League')\
    .getOrCreate()

json_data = json.dumps(response.json()['api']['leagues'])
br_league = sc.parallelize([json_data])
#br_league = sc.parallelize([response.text])
get_brazilian_leagues(spark, br_league)
spark.stop()
