# ambari user with necessary rights to request services and alerts status
user = ""

# user password
passwd = ""

# resolvable name of the Ambari server
nodeName = ""

# name of the cluster managed by Ambari
clusterName = ""

# the port where Ambari is listening
port = ""

# if Ambari is configured in https put "y" if not, put "n"
https = ""

# by default verify is set to false. you can set to the CA_BUNDLE path to avoid warnings
verify = False

# auth token for the api, do not touch unless if necessary
auth_values = (user, passwd)