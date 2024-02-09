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


# Displays instructions / information
def instructions():

    print("This program converts measurements of time, mass, and distance")
    sleep(1.5)
    print("Please choose a unit to convert from and a unit to convert to")
    sleep(1.5)
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to")
    return ""


# Main Routine goes here

# Display instructions if user has not used the program before
first_time = yes_no("Do you want to read the instructions? ").lower()

if first_time == "yes":
    instructions()
elif first_time == "no":
    pass
else:
    print("<ERROR> Please answer yes / no")