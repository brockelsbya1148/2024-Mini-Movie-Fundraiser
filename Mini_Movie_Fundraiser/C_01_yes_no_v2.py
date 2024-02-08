from time import sleep
# Functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response "n":
            return "no"

        else:
            print("please enter yes or no")

# Displays instructions / information
def instructions():

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

# Display instructions if user has not used the program before
first_time = input("Do you want to read the instructions? ").lower()

if first_time == "yes" or first_time == "y":
    instructions()
elif first_time == "no" or first_time == "n":
    pass
else:
    print("<ERROR> Please answer yes / no")