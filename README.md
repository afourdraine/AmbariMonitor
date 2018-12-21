# AmbariMonitor

The purpose of AmbariMonitor is to allow batch check of Ambari Alerts and Service Checks. It is configurable via the var files and the output is in fully formated json.

Check Ambari Alerts output example :
```
Checking Ambari alert
Number of Ambari alerts Checked :96
Number of Ambari alerts in maintenance mode : 0
Number of Ambari alerts OK : 91
Number of Ambari alerts NOK : 5
Failed alerts details :
{
    "HDFS Storage Capacity Usage (Daily)": {
        "message :": "The variance for this alert is 457834026B which is 45% of the 1025631222B average (307689367B is the limit)",
        "severity :": "WARNING"
    },
    "NameNode Service RPC Processing Latency (Daily)": {
        "message :": "Service RPC port is not enabled.",
        "severity :": "UNKNOWN"
    },
    "NameNode Service RPC Processing Latency (Hourly)": {
        "message :": "Service RPC port is not enabled.",
        "severity :": "UNKNOWN"
    },
    "NameNode Service RPC Queue Latency (Daily)": {
        "message :": "Service RPC port is not enabled.",
        "severity :": "UNKNOWN"
    },
    "NameNode Service RPC Queue Latency (Hourly)": {
        "message :": "Service RPC port is not enabled.",
        "severity :": "UNKNOWN"
    }
}
```

Check Ambari Services output example :
```
Checking Ambari services, please wait
SCHEDULED
Number of Services Checked :10
Number of Services Check failed : 1
{
    "Hive Service Check": "FAILED"
}

Process finished with exit code 0
```

## Getting Started

Download the repository or clone it :

```
it clone https://github.com/afourdraine/AmbariMonitor.git
```

Make the python script executable :

```
chmod -R +x ./AmbariMonitor
```

### Prerequisites

AmbariMonitor use the following python modules:

```
import requests
import json
import urllib3
import os
```

### Installing

A step by step guide to launch AmbariMonitor

Before launching the script, change the cluster related variable in the var.py file :
 ```
 # ambari user with necessary rights to request services and alerts status
user = "admin"

# user password
passwd = "MyPassw0rd"

# resolvable name of the Ambari server
nodeName = "ambari0.my.domain.com"

# name of the cluster managed by Ambari
clusterName = "MyCluster"

# the port where Ambari is listening
port = "8080"

# if Ambari is configured in https put "y" if not, put "n"
https = "n"

# by default verify is set to false. you can set to the CA_BUNDLE path to avoid warnings
verify = False

# auth token for the api, do not touch unless if necessary
auth_values = (user, passwd)
```

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

