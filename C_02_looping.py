# main routine starts here

# set maximum number of tickets
MAX_TICKETS = 3

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit ")

    if name == 'xxx':
        break

    else:
        tickets_sold += 1
# Output number of tickets sold
if tickets_sold == 3:
    print()
    print("Congratulations, you sold all the available tickets")
else:
    print("You have sold", tickets_sold, "ticket/s. There are", MAX_TICKETS - tickets_sold, "ticket/s remaining")