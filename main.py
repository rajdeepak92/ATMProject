import json
from user_registration import register_user
from user_login import login
from check_balance import check_balance
from add_withdraw_balance import add_balance, withdraw_balance
from change_password import change_password


def main():
    user_data = {}
    while True:
        print("Welcome to the ATM machine")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register_user(user_data)
        elif choice == "2":
            user = login(user_data)
            if user:
                while True:
                    print("Welcome", user["name"])
                    print("1. Check balance")
                    print("2. Add balance")
                    print("3. Withdraw balance")
                    print("4. Change password")
                    print("5. Logout")
                    choice = input("Enter your choice: ")
                    if choice == "1":
                        check_balance(user)
                    elif choice == "2":
                        add_balance(user)
                    elif choice == "3":
                        withdraw_balance(user)
                    elif choice == "4":
                        change_password(user, user_data)
                    elif choice == "5":
                        break
                    else:
                        print("Invalid choice")
            else:
                print("Invalid userid or pin")
        elif choice == "3":
            with open("user_data.json", "w") as file:
                json.dump(user_data, file)
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
