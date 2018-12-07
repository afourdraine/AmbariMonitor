# run
from var import *
from servicesAlert.function import *

failed = {}
maintenance = {}
failed_test = 0
maintenance_test = 0
total_test = 0
good_test = 0

serviceAlert = getServicesAlert(nodeName, clusterName, auth_values)

for item in serviceAlert["items"]:

    total_test += 1

    if item["Alert"]["state"] != "OK":


        if item["Alert"]["maintenance_state"] == "OFF":

            failed_test += 1

            failed.update({item["Alert"]["label"]: item["Alert"]["text"]})

        else:

            maintenance_test += 1

            maintenance.update({item["Alert"]["label"]: item["Alert"]["text"]})

    if item["Alert"]["state"] == "OK":

        good_test += 1

print("Number of Ambari alerts Checked :" + str(total_test))
print("Number of Ambari alerts in maintenance mode : " + str(maintenance_test))
print("Number of Ambari alerts OK : " + str(good_test))
print("Number of Ambari alerts NOK : " + str(failed_test))

if failed:
    failed_alert = json.dumps(failed)
    failed_alert = json.loads(failed_alert)

    print("Failed alerts details :")
    print(json.dumps(failed_alert, indent=4, sort_keys=True))

if maintenance:
    print("Alerts of services in maintenance mode :")
    for item in maintenance:
        print(item)

else:
    print("Number of Services Checked :" + str(total_test))
    print("Number of Services Check failed : " + str(failed_test))