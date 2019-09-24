package sql

import org.apache.spark.SparkConf;
import org.apache.spark.sql.SparkSession;

class SimpleQuery(var masterURL: String) {
  require(masterURL != "", "URL Master must be informed")

  def firstQuery()
    {
      val conf = new SparkConf().setMaster(masterURL).setAppName("FirstQuery");
      val spark = SparkSession.builder().appName("Spark SQL basic example").config(conf).getOrCreate();

      //var usersDF = spark.read.format("csv").option("sep","|").option("heard","true").option("inferSchema", "true").load("file:///C:/Users/vascora/Desktop/study/learning-journey/spark-projects/src/main/datasources/sunroof_project.csv");
      var usersDF = spark.read.format("csv").option("delimiter","|").option("heard","false").option("inferSchema", "true").load("file:///C:/Users/vascora/Documents/EY Sydney/Data/ECD_2017_MERCK_ULTIMO.txt");
      usersDF.show(1000,false) ;
    }
}
