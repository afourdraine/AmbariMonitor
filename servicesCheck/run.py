#run
from servicesCheck.var import *
from servicesCheck.funtion import *

serviceCheck = runServicesCheck(nodeName, clusterName, auth_values)

batchId = serviceCheck["resources"][0]["RequestSchedule"]["id"]
batchId = str(batchId)
batchStatus = getBachStatus(nodeName, clusterName, auth_values, batchId)

print(batchStatus)
while batchStatus == "SCHEDULED":
    batchStatus = getBachStatus(nodeName, clusterName, auth_values, batchId)

    parse = getServicesCheck(nodeName, clusterName, auth_values)

    final = {}
    failed = {}
    failed_test = 0
    total_test = 0

    for item in parse["items"]:

        if item["Requests"]["request_status"] == "COMPLETED" and item["Requests"]["request_context"] not in final:

            final.update({item["Requests"]["request_context"]: item["Requests"]["request_status"]})

            total_test += 1

        elif item["Requests"]["request_status"] == "FAILED" and item["Requests"]["request_context"] not in final:

            final.update({item["Requests"]["request_context"]: item["Requests"]["request_status"]})

            failed.update({item["Requests"]["request_context"]: item["Requests"]["request_status"]})

            failed_test += 1

            total_test += 1

if failed:
    print("Number of Services Checked :" + str(total_test))
    print("Number of Services Check failed : " + str(failed_test))
    print(failed)
else:
    print("Number of Services Checked :" + str(total_test))
    print("Number of Services Check failed : " + str(failed_test))
    print(final)






