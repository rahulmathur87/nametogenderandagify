import requests


class InfoBot:
    def __init__(self, name):
        self.name = name

    def get_age(self):
        endpoint = 'https://api.agify.io'
        params = {
            'name': self.name
        }

        response = requests.get(url=endpoint, params=params)
        response.raise_for_status()
        return response.json()['age']

    def get_gender(self):
        endpoint = 'https://api.genderize.io'
        params = {
            'name': self.name
        }

        response = requests.get(url=endpoint, params=params)
        response.raise_for_status()
        return response.json()['gender']
    