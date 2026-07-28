account_name = input("Enter Account Holder Name: ")

correct_pin = 1234
balance = 10000
transactions = []

attempt = 0

while attempt < 3:

    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:

        print("Login Successful")

        while True:

            print("\n------ ATM MENU ------")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transactions")
            print("5. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Available Balance:", balance)
                transactions.append("Checked Balance : " + str(balance))

            elif choice == 2:
                amount = float(input("Enter deposit amount: "))
                balance = balance + amount
                transactions.append("Deposited : " + str(amount))
                print("Amount Deposited Successfully")

            elif choice == 3:
                amount = float(input("Enter withdraw amount: "))

                if amount <= balance:
                    balance = balance - amount
                    transactions.append("Withdrawn : " + str(amount))
                    print("Please collect your cash")
                else:
                    print("Insufficient Balance")

            elif choice == 4:
                print("Transaction History")

                if len(transactions) == 0:
                    print("No Transactions")
                else:
                    for i in transactions:
                        print(i)

            elif choice == 5:
                print("Thank You for Using ATM")
                break

            else:
                print("Invalid Choice")

        break

    else:
        attempt = attempt + 1
        print("Wrong PIN")
        print("Attempts Left:", 3 - attempt)

if attempt == 3:
    print("Card Blocked")
