

def get_brazilian_leagues(spark, json_br_league):
    df = spark.read.json(json_br_league)
    df.printSchema()
    #df.show()

    df.createOrReplaceTempView('vw_brasileirao')

    df1 = spark.sql("""
    select country
          ,country_code
          ,coverage.fixtures.events
          ,coverage.fixtures.lineups
          ,coverage.fixtures.players_statistics
          ,coverage.fixtures.statistics
          ,coverage.odds
          ,coverage.players
          ,coverage.predictions
          ,coverage.standings
          ,coverage.topScorers
          ,flag
          ,is_current
          ,league_id
          ,logo
          ,name
          ,season
          ,season_start
          ,season_end
          ,standings
          ,type
    from vw_brasileirao
    """)
    df1.show()


#if __init__ == "__main__":
#    spark =  SparkSession \
#             .builder \
#             .appName('Python Spark to analyse Brazilian League') \
#             #.config('spark.some.config.option', 'some-value') \
#             .getOrCreate()

#    get_brazilian_leagues(spark, leagues=[])
