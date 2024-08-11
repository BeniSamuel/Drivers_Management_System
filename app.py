import handlers

drivers=[]
def main():

    while True:
        print("\nWelcome to Drivers System\n1. Add Driver\n2. Delete Driver\n3. Search Driver\n4. Update Driver\n5. Display Driver\n6. Exist")
        choice=int(input("Enter choice: "))

        match choice:
            case 1:
                handlers.addDriver(drivers)
            case 2:
                handlers.deleteDriver(drivers)
            case 3:
                handlers.searchDriver(drivers)
            case 4:
                handlers.updateDriver(drivers)
            case 5:
                handlers.displayDriver(drivers)
            case 6:
                print("Existing Program Byee!!")
                break
            case _:
                print("Invalid choice")



main()