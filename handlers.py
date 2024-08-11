def addDriver(drivers):
    name=input("Enter name: ").lower()
    car=input("Enter type of Car: ").lower()
    drivers.append({"name":name,"car":car})


def deleteDriver(drivers):
    name=input("Enter name: ").lower()
    for driver in drivers:
        if driver["name"].lower() == name:
            drivers.remove(driver)
            print(f"Removed {name}")



def searchDriver(drivers):
    name=input("Enter name: ").lower()
    for driver in drivers:
        if driver["name"].lower() == name:
            print(f" name: {driver["name"]} car: {driver["car"]}")
        else:
            print("Driver not registered")



def updateDriver(drivers):
    name=input("Enter name: ").lower()
    car=input("Enter car type: ").lower()

    for driver in drivers:
        if driver["name"].lower() == name:
            driver["name"]= name
            driver["car"]=car
            print(f" Updated name: {name} car: {car}")



def displayDriver(drivers):
    for idx, driver in enumerate(drivers,1):
        print(f" {idx}. name: {driver["name"]} car: {driver["car"]}")
