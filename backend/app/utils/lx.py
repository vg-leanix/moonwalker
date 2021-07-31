import requests
import json


def authenticate(host: str, apitoken: str):
    auth_url = 'https://'+host+'.leanix.net/services/mtm/v1/oauth2/token'
    response = requests.post(auth_url, auth=('apitoken', apitoken),
                             data={'grant_type': 'client_credentials'})

    if response.status_code == 200:
        access_token = response.json()['access_token']
        error = None

    elif response.status_code == 401:
        error = "API Token invalid."
        access_token = None

    return access_token, error
