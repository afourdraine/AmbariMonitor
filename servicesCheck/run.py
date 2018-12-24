#run
import sys
sys.path.append('.')
from var import *
from servicesCheck.function import *

serviceCheck = runServicesCheck(nodeName, port, clusterName, auth_values, https, verify)

batchId = serviceCheck["resources"][0]["RequestSchedule"]["id"]
batchId = str(batchId)
batchStatus = getBachStatus(nodeName, port, clusterName, auth_values, batchId, https, verify)

print(batchStatus)
while batchStatus == "SCHEDULED":
    batchStatus = getBachStatus(nodeName, port, clusterName, auth_values, batchId, https, verify)

    parse = getServicesCheck(nodeName, port, clusterName, auth_values, https, verify)

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

            total_test += 1

            failed_test += 1

if failed:
    print("Number of Services Checked :" + str(total_test))
    print("Number of Services Check failed : " + str(failed_test))
    print(json.dumps(failed, indent=4, sort_keys=True))
else:
    print("Number of Services Checked :" + str(total_test))
    print("Number of Services Check failed : " + str(failed_test))
    print(json.dumps(final, indent=4, sort_keys=True))






