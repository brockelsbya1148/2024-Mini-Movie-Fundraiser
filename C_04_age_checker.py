def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter a number")


tickets_sold = 0

while True:

    name = input("Enter your name / xxx to quit ")

    if name == "xxx":
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
