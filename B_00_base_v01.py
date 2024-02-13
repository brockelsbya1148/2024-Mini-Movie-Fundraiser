from time import sleep
# Functions go here


def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            print()
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("<ERROR> Please enter yes/no")


# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response if blank, outputs error
        if response == "":
            print("Enter a name")
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

    statement_generator("Instructions / Information", "=")
    print("Please choose a unit to convert from and a unit to convert to")
    sleep(1)
    print("This program converts measurements of time, mass, and distance")
    sleep(1)
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key")
    return ""


# Main Routine goes here

# Heading
statement_generator("Conversion Calculator for Weight, Distance & Time", "-")

# Display instructions if user has not used the program before
first_time = yes_no("Do you want to read the instructions? ").lower()

if first_time == "yes":
    instructions()
elif first_time == "no":
    pass

# Set maximum number of tickets
MAX_TICKETS = 3
tickets_sold = 0

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    print()
    name = not_blank("Enter your name or 'xxx' to quit ")

    if name == 'xxx':
        break

    age = num_check("Age: ")

    if 21 <= age <= 120:
        pass
    elif age < 12:
        print("Your too young for this movie, go kick rocks loser")
        continue
    else:
        print("Too old for this movie, move along grandpa")
        continue

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == 3:
    print()
    print("Congratulations, you sold all the available tickets")
else:
    print("You have sold", tickets_sold, "ticket/s. There are", MAX_TICKETS - tickets_sold, "ticket/s remaining")