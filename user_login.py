def login(user_data):
    userid = input("Enter userid: ")
    pin = input("Enter pin: ")
    if userid in user_data and user_data[userid]["pin"] == pin:
        return user_data[userid]
    else:
        return None
