# Background
This python program is a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.

# Location of GIT repository
[https://github.com/mattledevs/customer_banking](https://github.com/mattledevs/customer_banking)

# Function of Customer Banking
The Customer Banking program consists of the files: Accounts.py, savings_account.py, cd_account.py, and customer_banking.py. The Accounts.py file contains the Account class with methods to set the balance and interest.

> ## savings_account.py
In the savings_account.py file, the Account class contains a create_savings_account function that will create a savings account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

> ## cd_account.py
In the cd_account.py file, the Account class contains a create_cd_account function that will create a CD account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

> ## customer_banking.py
In the customer_banking.py file, the create_savings_account and create_cd_account functions are imported to create a main function that prompts the user to enter the savings and CD account details, call the corresponding functions to calculate the interest earned and update the balances, and display the results.

# Future Work
Though this is a very rudimentary program illustrating the functionality and usefulness of creating and importing classes, this kind of banking system is far from being functional as it lacks security and user-entry data error handling. Future work could include integrating other kinds of investment systems and calculating returns. There should also be an option for the user to project returns when adding monthly or yearly to the account. Other functionality could be added like a debit system, that allows customers to move money between different accounts as well as withdrawing and depositing. 

