# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

    if var_age < 16:
        price = 7.50

    elif var_age < 65:
        price = 10.50

    else:
        price = 6.50

    return price


# Loop for testing
while True:

    # Get age (assume users input a valid integer
    age = int(input("Age: "))

    # Calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket price: ${:.2f}".format(age, ticket_cost))