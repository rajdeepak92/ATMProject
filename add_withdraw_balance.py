def add_balance(user):
    amount = int(input("Enter amount to add: "))
    user["balance"] += amount
    print("Balance added successfully")


def withdraw_balance(user):
    amount = int(input("Enter amount to withdraw: "))
    if user["balance"] >= amount:
        user["balance"] -= amount
        print("Balance withdrawn successfully")
    else:
        print("Insufficient balance")
