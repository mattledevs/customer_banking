# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    while True:
        try:
            savings_balance = float(input("What's your starting savings balance?"))
            break
        except ValueError:
            print("Please enter a valid number for the savings balance.")
    while True:
        try:
            savings_interest = float(input("What's the savings interest rate?"))
            break
        except ValueError:
            print("Please enter a valid number for the savings interest rate.")
    while True:
        try:
            savings_maturity = int(input("How many months will you be saving for?"))
            break
        except ValueError:
            print("Please enter a valid number of months for your savings account.")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your updated savings balance is ${updated_savings_balance:.2f}")
    print(f"Your interest earned with a savings account is ${interest_earned:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    while True:
        try:
            cd_balance = float(input("What's your starting CD balance?"))
            break
        except ValueError:
            print("Please enter a valid number for the CD balance.")
    while True:
        try:
            cd_interest = float(input("What's the CD interest rate?"))
            break
        except ValueError:
            print("Please enter a valid number for the CD interest rate.")
    while True:
        try:
            cd_maturity = int(input("How many months will you be saving for?"))
            break
        except ValueError:
            print("Please enter a valid number of months for your CD account.")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your updated CD balance is ${updated_cd_balance:.2f}")
    print(f"Your interest earned with a CD account is ${interest_earned:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()