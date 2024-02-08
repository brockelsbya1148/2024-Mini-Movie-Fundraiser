from time import sleep
# Functions go here


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
    print()
    sleep(1)
    print("This program converts measurements of time, mass, and distance")
    print()
    sleep(1)
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit")
    print()
    return ""


# Main Routine goes here

# Heading
statement_generator("Conversion Calculator for Weight, Distance & Time", "-")

# Display instructions if user has not used the program before
first_time = input("Do you want to read the instructions? ").lower()

if first_time == "yes":
    instructions()
elif first_time == "no":
    pass
else:
    print("<ERROR> Please answer yes / no")


# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":
    # Ask the user for the file type
    data_type = user_choice()
    print()
    print("You chose", data_type)
    print()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()