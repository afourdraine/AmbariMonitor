import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getServicesAlert(nodeName, port, clusterName, auth_values, https, verify):

    if https == "n":

        url = "http://" + nodeName + ":" + port + "/api/v1/clusters/" + clusterName + "/alerts"

    elif https == "y":

        url = "https://" + nodeName + ":" + port + "/api/v1/clusters/" + clusterName + "/alerts"

    else:

        exit("[servicesAlert] could not run because of : bad value provided. Please check the https var")

    querystring = {"fields": "*"}

    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "7eb64f13-6076-4c96-a5c3-d0de174b5df9"
        }

    response = requests.request("GET", url, headers=headers, params=querystring, auth=auth_values, verify=verify)

    result = json.loads(response.text)

    return result
