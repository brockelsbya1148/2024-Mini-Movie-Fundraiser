from time import sleep
# Functions go here


def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            print()
            return "yes"

        elif response == "no" or response == "n":
            print()
            return "no"


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
else:
    print("<ERROR> Please answer yes / no")