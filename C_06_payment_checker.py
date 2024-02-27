from time import sleep


# Functions go here
def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            print()
            return "cash"

        elif response == "credit" or response == "cr":
            print()
            return "credit"


# Main Routine goes here
while True:

    payment_method = cash_credit("Choose a payment method (cash or credit) ").lower()

    print("You chose", payment_method)
    print()
