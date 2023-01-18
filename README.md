# __Project ATM Application__

# Overview

-   __This is a simple ATM machine simulation that allows users to register, login, check their balance, add or withdraw money, and change their password. The application stores all user data in a separate JSON file.__

## __Getting Started__

1.Clone the repository and navigate to the project directory

2.Run python main.py to start the application

3.Follow the prompts to register, login, and perform various actions

## __User Registration__

Users can register by providing a unique userid, name, date of birth, and pin. Once registered, the user's data is stored in a separate JSON file.

## __User Login__

Users can log in by providing their userid and pin. If the userid and pin match the data stored in the JSON file, the user is granted access to the system.

## __Check Balance__

Once logged in, users can check their balance by selecting the appropriate option. The balance will be displayed on the screen.

## __Add Balance__

Users can add money to their account by providing the desired amount. The balance will be updated in the JSON file and displayed on the screen.

## __Withdraw Balance__

Users can withdraw money from their account by providing the desired amount. The balance will be updated in the JSON file and displayed on the screen. If the user has insufficient funds, an error message will be displayed.

## __Change Password__

Users can change their password by providing their previous password and date of birth. If the previous password and date of birth match the data stored in the JSON file, the user can enter a new password. The password will be updated in the JSON file.

## __LOGIUT__

Users can logout by selecting the appropriate option. Any changes made to the user's data will be saved in the JSON file before logging out.

## __File Descriptions__

-   `main.py` - This is the main file that runs the application. It imports functionality from other files and handles user input
-   `user_registration.py` - This file contains the code for registering users
-   `user_login.py` - This file contains the code for logging in users
-   `check_balance.py` - This file contains the code for checking a user's balance
-   `add_withdraw_balance.py` - This file contains the code for adding and withdrawing money from a user's account
-   `change_password.py` - This file contains the code for changing a user's password
-   `user_data.json` - This is the JSON file where user data is stored

## __Code Optimization__

The code has been optimized to have a time complexity of O(n) or log(n) as much as possible.

# __NOTE/CONCLUSION__

This is an example of an ATM machine simulation that can be used as a starting point for a more complex project. It demonstrates how to use multiple files to organize code, handle user input, and store data in a JSON file.
