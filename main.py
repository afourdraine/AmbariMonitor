import os

# array with function to be launch at the end of the main section
selector = {}

# cursor in order to access and control while loop
cursor = "empty_var"

print("Choose functions to launch")

while cursor != "y" and cursor != "n":

    cursor = input("all           [n/y] : ")

    # store user choice
    selector.update({"all": str(cursor)})

# reset cursor in order to enter into next while loop
cursor = ""

# if all is selected, there is no need to ask for the rest of the functions
if selector["all"] != "y":

    while cursor != "y" and cursor != "n":

        cursor = input("servicesCheck [n/y] : ")

        selector.update({"servicesCheck": str(cursor)})

    cursor = ""

    while cursor != "y" and cursor != "n":

        cursor = input("servicesAlert [n/y] : ")

        selector.update({"servicesAlert": str(cursor)})

if selector["all"] == "y":

    print("Launching check servicesAlert")
    os.system("python servicesAlert/run.py")

    print("Launching servicesCheck, please wait")
    os.system("python servicesCheck/run.py")

else:

    if selector["servicesAlert"] == "y":

        print("Checking Ambari alert")
        os.system("python servicesAlert/run.py")

    if selector["servicesCheck"] == "y":

        print("Checking Ambari services, please wait")
        os.system("python servicesCheck/run.py")




