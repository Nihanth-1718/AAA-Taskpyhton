import random
from datetime import datetime

print("================================")
print("     CineBook Ticket System")
print("================================")

name = input("\nEnter Your Name: ")

print("\nSelect Movie Genre")
print("1. Action")
print("2. Comedy")
print("3. Horror")
print("4. Romance")

choice = input("Enter Your Choice: ")

if choice == "1":
    movies = ["Salaar", "Pushpa 2", "Kalki 2898 AD", "RRR", "KGF Chapter 2"]

elif choice == "2":
    movies = ["MAD Square", "Jathi Ratnalu", "DJ Tillu", "F3", "Brochevarevarura"]

elif choice == "3":
    movies = ["Virupaksha", "Masooda", "Stree 2", "Bramayugam", "The Conjuring"]

elif choice == "4":
    movies = ["Sita Ramam", "Hi Nanna", "Love Today", "Premalu", "96"]

else:
    print("Invalid Choice")
    exit()

print("\nAvailable Movies")

count = 1
for movie in movies:
    print(count, ".", movie)
    count += 1

selected_movie = input("\nEnter Movie Name: ")

if selected_movie in movies:

    show_times = [
        "10:00 AM",
        "1:00 PM",
        "4:00 PM",
        "7:00 PM",
        "10:00 PM"
    ]

    show = random.choice(show_times)

    today = datetime.now().strftime("%d-%m-%Y")

    print("\n========== BOOKING CONFIRMED ==========")
    print("Customer Name :", name)
    print("Movie         :", selected_movie)
    print("Show Time     :", show)
    print("Booking Date  :", today)
    print("=======================================")
    print("Enjoy Your Movie!")

else:
    print("Sorry! Movie is not available.")
