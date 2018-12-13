# run
from var import *
from servicesAlert.function import *

failed = {}
maintenance = {}
nb_failed_test = 0
nb_maintenance_test = 0
nb_total_test = 0
nb_good_test = 0

serviceAlert = getServicesAlert(nodeName, port, clusterName, auth_values, https, verify)

for item in serviceAlert["items"]:

    nb_total_test += 1

    if item["Alert"]["state"] != "OK":

        if item["Alert"]["maintenance_state"] == "OFF":

            nb_failed_test += 1

            failed.setdefault(item["Alert"]["label"], {})["severity :"] = item["Alert"]["state"]
            failed.setdefault(item["Alert"]["label"], {})["message :"] = item["Alert"]["text"]

        else:

            nb_maintenance_test += 1

            maintenance.update({item["Alert"]["service_name"]: item["Alert"]["host_name"]})

    if item["Alert"]["state"] == "OK":

        nb_good_test += 1

print("Number of Ambari alerts Checked :" + str(nb_total_test))
print("Number of Ambari alerts in maintenance mode : " + str(nb_maintenance_test))
print("Number of Ambari alerts OK : " + str(nb_good_test))
print("Number of Ambari alerts NOK : " + str(nb_failed_test))

if maintenance:

    print("Services in maintenance mode :")

    for item in maintenance:

        print(item)

if failed:

    failed_alert = json.dumps(failed)

    failed_alert = json.loads(failed_alert)

    print("Failed alerts details :")
    print(json.dumps(failed_alert, indent=4, sort_keys=True))

else:

    print("Number of Services Checked :" + str(nb_total_test))
    print("Number of Services Check failed : " + str(nb_failed_test))
