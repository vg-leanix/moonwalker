import requests
import json



def authenticate(host:str, apitoken:str):
    auth_url = 'https://'+host+'.leanix.net/services/mtm/v1/oauth2/token'
    response = requests.post(auth_url, auth=('apitoken', apitoken),
                             data={'grant_type': 'client_credentials'})
    response.raise_for_status()
    access_token = response.json()['access_token']

    return access_token



def put_processor(host: str, jwt_token:str, processor:str):

    with open(processor) as f:
        processor_json = json.load(f)
    
    print(type(processor_json))
    print(processor_json)

    request_url = f'https://{host}.leanix.net/services/integration-api/v1/configurations'

    auth_header = 'Bearer ' + jwt_token
    header = {'Authorization': auth_header, "Content-Type": "application/json"}

    
    r = requests.put(request_url, json=processor_json, headers=header)
    print(r.raise_for_status())
    print(r)