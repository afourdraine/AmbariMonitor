# ambari user with necessary rights to request services and alerts status
user = "admin"

# user password
passwd = "afourdraine"

# resolvable name of the Ambari server
nodeName = "c154-node1"

# name of the cluster managed by Ambari
clusterName = "c154"

# the port where Ambari is listening
port = "8080"

# if Ambari is configured in https put "y" if not, put "n"
https = "n"

# by default verify is set to false. you can set to the CA_BUNDLE path to avoid warnings
verify = False

# auth token for the api, do not touch unless if necessary
auth_values = (user, passwd)