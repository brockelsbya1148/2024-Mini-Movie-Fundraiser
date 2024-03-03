from time import sleep
import pandas
import random
from datetime import date

# Functions go here


# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Your name can't be blank")
        else:
            return response


# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter a number")


# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

    if var_age < 16:
        price = 7.50

    elif var_age < 65:
        price = 10.50

    else:
        price = 6.50

    return price


# checks that users enter a valid response (e.g. yes/ no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "PLease choose {} or {}".format(valid_responses[0], valid_responses[1])

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Displays instructions / information
def instructions():

    statement_generator("Instructions", "=")
    print("For each ticket, enter ...")
    sleep(1.5)
    print("- The person's name (can't be blank)")
    sleep(1.6)
    print("- Age (between 12 and 120)")
    sleep(1.6)
    print("- Payment method (cash / credit)\n")
    sleep(2)
    print("When you have entered all the users, type 'xxx' to quit.\n")
    sleep(2.6)
    print("The program will then display the ticket details\n"
          "including the cost of each ticket, the total cost\n"
          "and the total profit.\n")
    sleep(4.8)
    print("This information will also be automatically written to a text file.")
    sleep(2.7)

    return ""

# Main Routine goes here


# Heading
statement_generator("Mini Movie Fundraiser", "-")

# Set maximum number of tickets
MAX_TICKETS = 5
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Display instructions if user has not used the program before
want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1, yes_no_list)

if want_instructions == "yes":
    instructions()
elif want_instructions == "no":
    pass


# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    print()
    name = not_blank("Enter your name or 'xxx' to quit ")

    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Your too young for this movie, go kick rocks loser")
        continue
    else:
        print("Too old for this movie, move along grandpa")
        continue

    # Calculate ticket cost
    ticket_cost = calc_ticket_price(age)

    # Get payment method
    pay_method = string_checker("Choose a payment method (Credit or cash): ", 2, payment_list)
    print(f"You paid with {pay_method}")

    if pay_method == "cash":
        surcharge = 0
    else:
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # Add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

# Create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# Calculate the profit (ticket - 5)
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Choose a winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# ***** Get current date for heading and filename *****
# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Currency Formatting (uses currency function
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

heading = "\n---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)


# Create strings for printing
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Ticket Sales: ${}".format(total)
total_profit = "Total Profit : ${}".format(profit)

sales_status = "\n*** All the tickets have been sold ***"

winner_heading = "\n---- Raffle Winner ----"
winner_text = "The winner of the raffle is {}. " \
              "They have won ${} ie: Their ticket is " \
              "free!".format(winner_name, total_won)

# List holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading, total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# Print output
for item in to_write:
    print(item)

# Write output to file
# Create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close file
text_file.close()

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("You sold all the available tickets")
else:
    print("You sold", tickets_sold, "ticket/s. There are", MAX_TICKETS - tickets_sold, "ticket/s remaining")
sleep(2)
