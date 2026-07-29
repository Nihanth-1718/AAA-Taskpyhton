bmi = {"Name": [], "BMI": []}
pin = 1234
balance = 5000
history = []

# Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Sum
def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n - 1)

# Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

while True:

    print("\n1.Factorial")
    print("2.Sum")
    print("3.BMI")
    print("4.Fibonacci")
    print("5.ATM")
    print("6.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        num = int(input("Enter Number: "))
        print("Factorial =", factorial(num))

    elif ch == 2:
        num = int(input("Enter Number: "))
        print("Sum =", sum_num(num))

    elif ch == 3:
        users = int(input("No of Users: "))

        for i in range(users):
            name = input("Name: ")
            wt = float(input("Weight(kg): "))
            ht = float(input("Height(m): "))

            value = round(wt / (ht ** 2), 2)

            bmi["Name"].append(name)
            bmi["BMI"].append(value)

            if value < 18.5:
                print("Underweight")
            elif value < 25:
                print("Normal")
            elif value < 30:
                print("Overweight")
            else:
                print("Obese")

        print(bmi)

    elif ch == 4:
        terms = int(input("Enter Terms: "))
        for i in range(terms):
            print(fib(i), end=" ")
        print()

    elif ch == 5:

        if int(input("Enter PIN: ")) == pin:

            while True:

                print("\n1.Balance")
                print("2.Deposit")
                print("3.Withdraw")
                print("4.History")
                print("5.Exit")

                op = int(input("Choice: "))

                if op == 1:
                    print("Balance =", balance)

                elif op == 2:
                    amt = float(input("Deposit: "))
                    balance += amt
                    history.append(f"Deposit {amt}")

                elif op == 3:
                    amt = float(input("Withdraw: "))
                    if amt <= balance:
                        balance -= amt
                        history.append(f"Withdraw {amt}")
                    else:
                        print("Insufficient Balance")

                elif op == 4:
                    if history:
                        for item in history:
                            print(item)
                    else:
                        print("No Transactions")

                elif op == 5:
                    break

                else:
                    print("Invalid Choice")
        else:
            print("Wrong PIN")

    elif ch == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
