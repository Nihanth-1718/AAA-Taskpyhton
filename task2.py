# 2. Even or Odd Number Checker

value = int(input("Enter a number: "))

if value == 0:
    print("Zero is neither even nor odd")
else:
    if value > 0:
        if value % 2 == 0:
            print("Positive Even Number")
        else:
            print("Positive Odd Number")
    else:
        if value % 2 == 0:
            print("Negative Even Number")
        else:
            print("Negative Odd Number")
