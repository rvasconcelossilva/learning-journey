from core.config import Config
import requests # package to manipulate api

class FootballApi():
    headers = {}
    config_file = ''

    def __init__(self):
        self.config_file = Config()
        self.headers = {
            'x-rapidapi-host': self.config_file.x_rapidapi_host,
            'x-rapidapi-key': self.config_file.x_rapidapi_key
            }

    def invoke_api(self, end_point):
        response = requests.get(self.config_file.url_rapidapi+end_point , headers=self.headers)
        return response

    def leagues(self, country,season=''):
        return self.invoke_api(f'/v2/leagues/country/{country}/{season}')
