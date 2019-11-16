import boto3
import botocore
import json #packge to handle json files

s3_resource = boto3.resource('s3')

def file_exists(json_file_name):
    try:
        #s3_resource.Object('football-data-sample', json_file_name)
        load_file(json_file_name)
        return True
    except botocore.exceptions.ClientError as e:
        return False

def load_file(json_file_name):
    try:
        return s3_resource.Object('football-data-sample', json_file_name).get()['Body'].read()
    except:
        raise

def upload_file(json_file_name):
     s3_resource.Bucket('football-data-sample').upload_file(Filename=json_file_name, Key=json_file_name)
