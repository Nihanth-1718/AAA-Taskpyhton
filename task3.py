# 3. Season Finder

month_num = int(input("Enter month number: "))

if month_num >= 1 and month_num <= 12:
    if month_num == 12 or month_num == 1 or month_num == 2:
        print("Season: Winter")
    elif month_num == 3 or month_num == 4 or month_num == 5:
        print("Season: Spring")
    elif month_num == 6 or month_num == 7 or month_num == 8:
        print("Season: Summer")
    else:
        print("Season: Autumn")
else:
    print("Invalid month entered")
