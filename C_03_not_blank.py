# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response if blank, outputs error
        if response == "":
            print("Enter a name")
        else:
            return response


while True:
    name = not_blank("Enter your name or 'xxx' to quit ")
    if name == "xxx":
        break

print("We are done")