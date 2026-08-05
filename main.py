from my_programs import *

while True:
    print("\n-- FUNCTION MENU --")
    print("1. Swap Two Numbers")
    print("2. GCD of Two Numbers")
    print("3. Reverse a Number")
    print("4. Sum of Digits")
    print("5. Count Vowels in a String")
    print("6. Check for Prime Number")
    print("7. Remove Duplicates from a List")
    print("8. Fibonacci Series")
    print("9. Check Even or Odd")
    print("10. Find Maximum in a List")
    print("11. Reverse a String")
    print("12. Count Uppercase and Lowercase Letters")
    print("13. Find Second Largest Number")
    print("14. Calculate Simple Interest")
    print("15. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        swap_numbers()

    elif choice == 2:
        gcd_numbers()

    elif choice == 3:
        reverse_number()

    elif choice == 4:
        sum_of_digits()

    elif choice == 5:
        count_vowels()

    elif choice == 6:
        check_prime()

    elif choice == 7:
        remove_duplicates()

    elif choice == 8:
        fibonacci_series()

    elif choice == 9:
        check_even_odd()

    elif choice == 10:
        find_maximum()

    elif choice == 11:
        reverse_string()

    elif choice == 12:
        count_case()

    elif choice == 13:
        second_largest()

    elif choice == 14:
        simple_interest()

    elif choice == 15:
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
