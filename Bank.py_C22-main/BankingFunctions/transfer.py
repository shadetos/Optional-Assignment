"""This function handles the transfer process for the user."""

# TODO: Pass in the checking_account and savings_account objects.
def handle_transfer(checking_account, savings_account):
    """
    Handles the transfer of funds between checking and savings accounts.

    Parameters:
    - checking (Account): The checking account object.
    - savings (Account): The savings account object.

    The function prompts the user to select an account to make a transfer.
    It handles exceptions and prints error messages if the user enters invalid inputs.
    If the user enters 'q', the function returns and exits.
    If the user enters '1', the function asks for the withdrawal amount from the checking account.
    If the user enters '2', the function asks for the withdrawal amount from the savings account.
    After the transfer the function prints the updated balances of both accounts.
    If the user enters an invalid choice, the function displays an error message and prompts again.
    """
    print("Which account would you like to transfer from?")
    # TODO: Prompt the user to select an account to transfer from.
    print("1. Checking")
    print("2. Savings")
    print("Q. Quit")
    choice = input("Enter your choice: ")

    # TODO: If the user chooses to quit, return from the function.
    choice = choice.upper()
    if choice == 'Q':
        return

    try:
        # TODO: If the selection is in a list of valid choices, i.e ['1', '2']
        if choice in ['1', '2']:
            try:
                # TODO: Prompt the user to enter the amount to transfer and convert it to a float.
                amount = float(input("Enter the amount to transfer: "))
            except ValueError:
                # TODO: Print an error message if the user enters an invalid amount.
                print("Invalid amount. Please enter a valid number.")
                # TODO: Call the handle_transfer function recursively if the user enters an invalid amount.
                handle_transfer(checking_account, savings_account)
                return

            # TODO: Add an if/else conditional statement to check the account choice,
            if choice == '1':
                # TODO: Call the withdraw and deposit methods on the appropriate account.
                print(f"Transferring ${amount:,.2f} from checking to savings.")
                checking_account.withdraw(amount)
                savings_account.deposit(amount)
            else:
                # TODO: Call the withdraw and deposit methods on the appropriate account.
                print(f"Transferring ${amount:,.2f} from savings to checking.")
                savings_account.withdraw(amount)
                checking_account.deposit(amount)
            # After the transfer call the balances function with the accounts.
            balances(checking_account, savings_account)
        else:
            # TODO: Raise a ValueError with a message stating the user entered an invalid choice.
            print("Invalid choice. Please enter '1' for Checking, '2' for Savings, or 'Q' to quit.")
    except ValueError as e:
        print(e)
        handle_transfer(checking_account, savings_account)

def balances(checking, savings):
    """This function prints the account balances for the user."""
    print("\nHere are your account balances:")
    print(f"Checking: ${checking.get_balance():,.2f}")
    print(f"Savings: ${savings.get_balance():,.2f}")
