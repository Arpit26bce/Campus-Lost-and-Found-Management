def admin_login():

    username = input("Enter Admin Username --> ")
    password = input("Enter Admin Password --> ")

    if username == "arpit" and password == "1234":
        print("Admin Login Successful")
        admin_menu()
    else:
        print("Invalid Username or Password !!")


def admin_menu():

    while True:

        print("----> ADMIN MENU <----")
        print("1. View Lost Items")
        print("2. View Found Items")
        print("3. View Claims")
        print("4. Approve Claim")
        print("5. Reject Claim")
        print("6. Exit")

        choice = input("Enter Your Choice --> ")

        if choice == '1':

            with open("lost.txt", "r") as f:
                x = f.read()

            print("---->  LOST ITEMS  <----")
            print(x)

        elif choice == '2':

            with open("found.txt", "r") as f:
                x = f.read()

            print("---->  FOUND ITEMS  <----")
            print(x)

        elif choice == '3':

            with open("claims.txt", "r") as f:
                x = f.read()

            print("---->  CLAIMS  <----")
            print(x)

        elif choice == '4':

            print("Claim approved.")

        elif choice == '5':

            print("Claim rejected.")

        elif choice == '6':
            break

        else:
            print("Invalid Choice !!")