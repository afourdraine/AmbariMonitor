import requests
import json


def getServicesAlert(nodeName, clusterName, auth_values):

    url = "http://" + nodeName + ":8080/api/v1/clusters/" + clusterName + "/alerts"

    querystring = {"fields": "*"}

    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "7eb64f13-6076-4c96-a5c3-d0de174b5df9"
        }

    response = requests.request("GET", url, headers=headers, params=querystring, auth=auth_values)

    result = json.loads(response.text)

    return result
