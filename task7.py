# Gold Locker Security System
# User gets 3 chances to enter the correct PIN.
# If the PIN is correct, the locker opens.
# The user can withdraw gold value.
# After 3 wrong attempts, the locker is locked for 24 hours.

pin = 1234
gold = 500000
chance = 3
while chance > 0:
    user_pin = int(input("Enter Locker PIN: "))
    if user_pin == pin:
        print("Correct PIN")
        print("Locker Opened")
        print("Gold Value = Rs.", gold)
        amount = int(input("Enter Gold Value to Withdraw: Rs. "))
        if amount <= gold:
            gold = gold - amount
            print("Gold Withdrawn Successfully")
            print("Remaining Gold Value = Rs.", gold)
        else:
            print("Not Enough Gold Value")

        break

    else:
        chance = chance - 1

        if chance > 0:
            print("Wrong PIN")
            print("Chances Left =", chance)
        else:
            print("Wrong PIN")
            print("Locker Locked for 24 Hours")
