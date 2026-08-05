import random
import smtplib
from email.mime.text import MIMEText


# Rock Paper Scissors

def play_game():
    print("\n--- Rock Paper Scissors ---")

    items = ["rock", "paper", "scissors"]

    user = input("Enter rock, paper or scissors: ").lower()

    if user not in items:
        print("Wrong Choice!")
        return

    computer = random.choice(items)

    print("Computer Selected:", computer)

    if user == computer:
        print("Match Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Won!")

    else:
        print("Computer Won!")


# Story Generator

def create_story():

    print("\n--- Story Generator ---")

    day = [
        "Yesterday",
        "Last Sunday",
        "One Morning",
        "Last Night"
    ]

    person = [
        "Rahul",
        "A Teacher",
        "A Little Boy",
        "My Friend"
    ]

    place = [
        "at School",
        "in Hyderabad",
        "near the Beach",
        "inside a Forest"
    ]

    action = [
        "found a treasure",
        "met an alien",
        "won a competition",
        "saved a puppy"
    ]

    ending = [
        "with great courage.",
        "using smart ideas.",
        "with the help of friends.",
        "by accident."
    ]

    story = (
        random.choice(day) + " " +
        random.choice(person) + " " +
        random.choice(place) + " " +
        random.choice(action) + " " +
        random.choice(ending)
    )

    print("\nGenerated Story:\n")
    print(story)


# OTP Email

def send_otp():

    print("\n--- OTP Generator ---")

    from_mail = input("Enter Sender Gmail: ")
    to_mail = input("Enter Receiver Gmail: ")
    password = input("Enter Gmail App Password: ")

    otp = random.randint(100000, 999999)

    text = MIMEText("Your OTP is: " + str(otp))

    text["Subject"] = "OTP Verification"
    text["From"] = from_mail
    text["To"] = to_mail

    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.starttls()

        mail.login(from_mail, password)

        mail.sendmail(from_mail, to_mail, text.as_string())

        mail.quit()

        print("OTP Sent Successfully!")
        print("OTP:", otp)

    except Exception as error:
        print("Something Went Wrong")
        print(error)


# BMI Calculator

def check_bmi():

    print("\n--- BMI Calculator ---")

    person_name = input("Enter Your Name: ")

    weight = float(input("Enter Weight in kg: "))
    height = float(input("Enter Height in meters: "))

    if weight <= 0 or height <= 0:
        print("Please Enter Valid Values")
        return

    result = weight / (height * height)

    print("BMI:", round(result, 2))

    if result < 18.5:
        print(person_name, "- Underweight")

    elif result < 25:
        print(person_name, "- Normal Weight")

    elif result < 30:
        print(person_name, "- Overweight")

    else:
        print(person_name, "- Obesity")


# Main Menu

while True:

    print("\n==========================")
    print("      MINI PROJECT MENU")
    print("==========================")
    print("1. Rock Paper Scissors")
    print("2. Story Generator")
    print("3. OTP Generator")
    print("4. BMI Calculator")
    print("5. Exit")

    option = input("Enter Your Choice: ")

    if option == "1":
        play_game()

    elif option == "2":
        create_story()

    elif option == "3":
        send_otp()

    elif option == "4":
        check_bmi()

    elif option == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice. Please Try Again.")
