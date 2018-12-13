import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def runServicesCheck(nodeName, port, clusterName, auth_values, https, verify):

    if https == "n":

        url = "http://" + nodeName + ":" + port + "/api/v1/clusters/" + clusterName + "/request_schedules"

    elif https == "y":

        url = "https://" + nodeName + ":" + port + "/api/v1/clusters/" + clusterName + "/request_schedules"

    else:

        exit("[servicesAlert] could not run because of : bad value provided. Please check the https var")


    payload = "[\n   {\n      \"RequestSchedule\":{\n         \"batch\":[\n            {\n               \"requests\":[\n                  {\n                     \"order_id\":1,\n                     \"type\":\"POST\",\n                      \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"HDFS Service Check\",\n                           \"command\":\"HDFS_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"HDFS\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":2,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"YARN Service Check\",\n                           \"command\":\"YARN_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"YARN\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":3,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"MapReduce Service Check\",\n                           \"command\":\"MAPREDUCE2_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"MAPREDUCE2\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":4,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"HBase Service Check\",\n                           \"command\":\"HBASE_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"HBASE\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":5,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Hive Service Check\",\n                           \"command\":\"HIVE_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"HIVE\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":6,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"WebHCat Service Check\",\n                           \"command\":\"WEBHCAT_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"WEBHCAT\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":7,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"PIG Service Check\",\n                           \"command\":\"PIG_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"PIG\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":8,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Falcon Service Check\",\n                           \"command\":\"FALCON_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"FALCON\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":9,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Storm Service Check\",\n                           \"command\":\"STORM_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"STORM\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":10,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Oozie Service Check\",\n                           \"command\":\"OOZIE_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"OOZIE\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":11,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Zookeeper Service Check\",\n                           \"command\":\"ZOOKEEPER_QUORUM_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"ZOOKEEPER\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":12,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Tez Service Check\",\n                           \"command\":\"TEZ_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"TEZ\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":13,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Sqoop Service Check\",\n                           \"command\":\"SQOOP_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"SQOOP\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":14,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Ambari Metrics Service Check\",\n                           \"command\":\"AMBARI_METRICS_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"AMBARI_METRICS\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":15,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Atlas Service Check\",\n                           \"command\":\"ATLAS_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"ATLAS\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":16,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Kafka Service Check\",\n                           \"command\":\"KAFKA_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"KAFKA\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":17,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Knox Service Check\",\n                           \"command\":\"KNOX_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"KNOX\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":18,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Spark Service Check\",\n                           \"command\":\"SPARK_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"SPARK\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":19,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"SmartSense Service Check\",\n                           \"command\":\"SMARTSENSE_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"SMARTSENSE\"\n                           }\n                        ]\n                     }\n                  },\n                  {\n                     \"order_id\":20,\n                     \"type\":\"POST\",\n                     \"uri\":\"/api/v1/clusters/"+clusterName+"/requests\",\n                     \"RequestBodyInfo\":{\n                        \"RequestInfo\":{\n                           \"context\":\"Ranger Service Check\",\n                           \"command\":\"RANGER_SERVICE_CHECK\"\n                        },\n                        \"Requests/resource_filters\":[\n                           {\n                              \"service_name\":\"RANGER\"\n                           }\n                        ]\n                     }\n                  }\n               ]\n            },\n            {\n               \"batch_settings\":{\n                  \"batch_separation_in_seconds\":1,\n                  \"task_failure_tolerance\":1\n               }\n            }\n         ]\n      }\n   }\n]"

    headers = {
        'X-Requested-By': "ambari",
        'Content-Type': "text/plain",
        'cache-control': "no-cache",
        'Postman-Token': "221c1530-1abc-401c-92c7-dc241adf0d67"
    }

    try:
        response = requests.request("POST", url, data=payload, headers=headers, auth=auth_values, verify=verify)
    except:
        print('An error occured during the request')

    result = json.loads(response.text)

    return result


def getBachStatus(nodeName, port, clusterName, auth_values, batchId, https, verify):

    if https == "n":

        url = "http://" + nodeName + ":" + port + "/api/v1/clusters/" + clusterName + "/request_schedules/" + str(batchId)

    elif https == "y":

        url = "https://" + nodeName + ":" + port + "/api/v1/clusters/" + clusterName + "/request_schedules/" + str(batchId)

    else:

        exit("[servicesAlert] could not run because of : bad value provided. Please check the https var")



    querystring = {"fields":"RequestSchedule/status"}

    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "7eb64f13-6076-4c96-a5c3-d0de174b5df9"
        }

    response = requests.request("GET", url, headers=headers, params=querystring, auth=auth_values, verify=verify)

    response_json = json.loads(response.text)

    batchStatus = response_json["RequestSchedule"]["status"]

    return batchStatus


def getServicesCheck(nodeName, port, clusterName, auth_values, https, verify):

    if https == "n":

        url = "http://" + nodeName + ":" + port + "/api/v1/clusters/" + clusterName + "/requests"

    elif https == "y":

        url = "https://" + nodeName + ":" + port + "/api/v1/clusters/" + clusterName + "/requests"

    else:

        exit("[servicesAlert] could not run because of : bad value provided. Please check the https var")

    querystring = {"fields": "Requests/id,Requests/request_status,Requests/request_context,Requests/request_schedule"}

    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "f8c468ef-05c4-4192-9ced-57ddbe6034fb"
    }

    response = requests.request("GET", url, headers=headers, params=querystring, auth=auth_values, verify=verify)

    parse = json.loads(response.text)

    return parse
