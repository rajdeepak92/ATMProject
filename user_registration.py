import json

def register_user(user_data):
    userid = input("Enter userid: ")
    if userid in user_data:
        print("Userid already exists")
    else:
        name = input("Enter name: ")
        dob = input("Enter date of birth (dd/mm/yyyy): ")
        pin = input("Enter pin: ")
        balance = 0
        user_data[userid] = {"name": name, "dob": dob, "pin": pin, "balance": balance}
        print("User registered successfully")
