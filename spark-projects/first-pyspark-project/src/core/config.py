import yaml # handle yaml files
import os
import rootpath # package to identify the root directory

class Config:
    url_rapidapi = ''
    x_rapidapi_host = ''
    x_rapidapi_key = ''
    config_file = ''

    def __init__(self):
        try:
            root_path = rootpath.detect()
            self.config_file = root_path+"/config.yml"
            with open(os.path.expanduser(self.config_file), 'r') as config_file:
                config_yaml = config_file.read() #read the file and load into a variable
                config_data = yaml.safe_load(config_yaml) #Deserialize the file into a dictionary
                self.url_rapidapi = config_data['url-rapidapi']
                self.x_rapidapi_host = config_data['x-rapidapi-host']
                self.x_rapidapi_key  = config_data['x-rapidapi-key']
        except FileNotFoundError:
            print(f'{config_file_path} has not been found. Check the config file path out.')
