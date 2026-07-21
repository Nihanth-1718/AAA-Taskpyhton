# 4. Weekend Budget Planner

print("=========== Weekend Budget Planner ===========")

amount = int(input("Enter your weekend budget: "))

if amount >= 0:
    if amount > 10000:
        print("Plan: Trip")
    elif amount > 5000:
        print("Plan: Resort Stay")
    elif amount > 3000:
        print("Plan: Movie and Dinner")
    elif amount > 1000:
        print("Plan: Cafe and Shopping")
    elif amount > 500:
        print("Plan: Street Food and Park Visit")
    else:
        print("Plan: Stay Home")
else:
    print("Please don't enter negative values")
