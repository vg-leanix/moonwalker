import requests
import json


def get_extensions(jwt_token: str):
    auth_header = 'Bearer ' + jwt_token
    header = {'Authorization': auth_header, 'accept': 'application/json'}

    endpoint = f'https://eu.leanix.net/services/provisioning/v1/extensions'

    res = requests.get(url=endpoint, headers=header)

    extensions = res.json()

    available_extensions = dict()
    for extension in extensions:
        if not extension['status'] == "End of Life":
            available_extensions[extension['name']] = extension['alias']

    return available_extensions


def provision_data_model(edition: str, jwt_token: str):

    endpoint = f'https://eu.leanix.net/services/provisioning/v1/provision'

    params = {"apply_base_model": True}
    auth_header = 'Bearer ' + jwt_token
    header = {'Authorization': auth_header, "Content-Type": "application/json"}
    available_extensions = get_extensions(jwt_token=jwt_token)
    error = ""
    print(available_extensions)
    
    if edition in available_extensions.keys():
        extension = available_extensions[edition]
        

        payload = {
            "extensions":[extension]
        }
        


        res = requests.put(url= endpoint, params=params, headers=header, json=payload)
        print(res.json())
        print(res.status_code)

        if res.status_code != 200:
            res_json = res.json()
            error=res_json['detail']['error']
    
    else:
        error = "Edition does not exist"


    return res.status_code, error
