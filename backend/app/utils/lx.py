import requests
import json



def authenticate(host:str, apitoken:str):
    auth_url = 'https://'+host+'.leanix.net/services/mtm/v1/oauth2/token'
    response = requests.post(auth_url, auth=('apitoken', apitoken),
                             data={'grant_type': 'client_credentials'})
    response.raise_for_status()
    access_token = response.json()['access_token']

    return access_token



