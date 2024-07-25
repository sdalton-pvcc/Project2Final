import random
import re

print("Welcome to the Magic 8-Ball. Where we answer all your questions!")

while True:
    question = input("Ask a question: (press enter to quit) ")
    if question == "":
        print("Goodbye, Thanks for stopping by!")
        break 
        # Validate input to contain only alphabetic characters and spaces
    if not re.match(r"^[A-Za-z\s]+$", question):
        print("Please enter a valid question containing only letters and spaces.")
        continue
    answer = random.randrange(1,20)
    print("Magic 8 Ball says: ")
    if answer == 1:
        print("Yes, Definetely")
    elif answer == 2:
        print("Without a Doubt")
    elif answer == 3:
        print("It is certain")
    elif answer == 4:
        print("It is decidedly")
    elif answer == 5:
        print("You may rely on it")
    elif answer == 6:
        print("Most Likely")
    elif answer == 7:
        print("Outlook seems good")
    elif answer == 8:
        print("Signs point to Yes!")
    elif answer == 9:
        print("Without a Doubt")
    elif answer == 10:
        print("You may rely on it")
    elif answer == 11:
        print("Please try again")
    elif answer == 12:
        print("Ask again later")
    elif answer == 13:
        print("Better not tell you right now")
    elif answer == 14:
        print("Cannot Predict Right now")
    elif answer == 15:
        print("Concentrate and ask again")
    elif answer == 16:
        print("Don't Count on it")
    elif answer == 17:
        print("My reply is No")
    elif answer == 18:
        print("My sources say no")
    elif answer == 19:
        print("Out look not so good")
    elif answer ==20:
        print("Very Doubtful")
    