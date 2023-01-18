def change_password(user, user_data):
    prev_password = input("Enter previous password: ")
    dob = input("Enter date of birth (dd/mm/yyyy): ")
    if user["pin"] == prev_password and user["dob"] == dob:
        new_password = input("Enter new password: ")
        user["pin"] = new_password
        print("Password changed successfully")
    else:
        print("Invalid previous password or date of birth")
