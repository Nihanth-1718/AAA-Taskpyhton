def swap_numbers():
    print("Program : Swap Two Numbers")

    print("\nCode:\n")

    print("""
def swap(a, b):
    a, b = b, a
    return a, b

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

x, y = swap(num1, num2)

print("After Swapping :", x, y)
""")

    print("Test Case 1")
    print("Input : swap(10, 20)")
    print("Expected Output : (20, 10)\n")

    print("Test Case 2")
    print("Input : swap(5, -1)")
    print("Expected Output : (-1, 5)\n")

    print("Logic:")
    print("This program swaps two numbers using tuple unpacking.")
    print("It swaps the values without using a temporary variable.\n")

    print("User Execution")
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))

    x, y = swap(num1, num2)

    print("After Swapping :", x, y)


def swap(a, b):
    a, b = b, a
    return a, b






def gcd_numbers():
    print("Program : GCD of Two Numbers")

    print("\nCode:\n")

    print("""
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

print("GCD :", gcd(num1, num2))
""")

    print("Test Case 1")
    print("Input : gcd(24, 36)")
    print("Expected Output : 12\n")

    print("Test Case 2")
    print("Input : gcd(15, 25)")
    print("Expected Output : 5\n")

    print("Logic:")
    print("This program finds the Greatest Common Divisor (GCD) of two numbers.")
    print("It uses the Euclidean Algorithm by repeatedly finding the remainder.\n")

    print("User Execution")
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))

    print("GCD :", gcd(num1, num2))


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a






def reverse_number():
    print("Program : Reverse a Number")

    print("\nCode:\n")

    print("""
num = int(input("Enter a Number : "))

rev = 0
temp = num

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed Number :", rev)
""")

    print("Test Case 1")
    print("Input : 12345")
    print("Expected Output : 54321\n")

    print("Test Case 2")
    print("Input : 9087")
    print("Expected Output : 7809\n")

    print("Logic:")
    print("This program reverses a number by extracting its digits one by one.")
    print("Each extracted digit is added to the reversed number in reverse order.\n")

    print("User Execution")
    num = int(input("Enter a Number : "))

    rev = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    print("Reversed Number :", rev)






def sum_of_digits():
    print("Program : Sum of Digits")

    print("\nCode:\n")

    print("""
num = int(input("Enter a Number : "))

total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("Sum of Digits :", total)
""")

    print("Test Case 1")
    print("Input : 1234")
    print("Expected Output : 10\n")

    print("Test Case 2")
    print("Input : 567")
    print("Expected Output : 18\n")

    print("Logic:")
    print("This program finds the sum of all digits in a number.")
    print("It extracts each digit using the modulus operator and adds it to the total.\n")

    print("User Execution")
    num = int(input("Enter a Number : "))

    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10

    print("Sum of Digits :", total)






def count_vowels():
    print("Program : Count Vowels in a String")

    print("\nCode:\n")

    print("""
text = input("Enter a String : ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of Vowels :", count)
""")

    print("Test Case 1")
    print("Input : Hello World")
    print("Expected Output : 3\n")

    print("Test Case 2")
    print("Input : Python Programming")
    print("Expected Output : 4\n")

    print("Logic:")
    print("This program counts the number of vowels in a given string.")
    print("It checks each character and increases the count if it is a vowel.\n")

    print("User Execution")
    text = input("Enter a String : ")

    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    print("Number of Vowels :", count)






def check_prime():
    print("Program : Check for Prime Number")

    print("\nCode:\n")

    print("""
num = int(input("Enter a Number : "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is Not a Prime Number")
            break
    else:
        print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")
""")

    print("Test Case 1")
    print("Input : 17")
    print("Expected Output : 17 is a Prime Number\n")

    print("Test Case 2")
    print("Input : 18")
    print("Expected Output : 18 is Not a Prime Number\n")

    print("Logic:")
    print("This program checks whether a number is prime or not.")
    print("It tests divisibility from 2 to num-1. If divisible, it is not prime; otherwise, it is prime.\n")

    print("User Execution")
    num = int(input("Enter a Number : "))

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is Not a Prime Number")
                break
        else:
            print(num, "is a Prime Number")
    else:
        print(num, "is Not a Prime Number")



def remove_duplicates():
    print("Program : Remove Duplicates from a List")

    print("\nCode:\n")

    print("""
numbers = list(map(int, input("Enter list elements separated by space : ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates :", unique)
""")

    print("Test Case 1")
    print("Input : [1, 2, 2, 3, 4, 4, 5]")
    print("Expected Output : [1, 2, 3, 4, 5]\n")

    print("Test Case 2")
    print("Input : [10, 20, 10, 30, 20]")
    print("Expected Output : [10, 20, 30]\n")

    print("Logic:")
    print("This program removes duplicate elements from a list.")
    print("It checks each element and adds it to a new list only if it is not already present.\n")

    print("User Execution")
    numbers = list(map(int, input("Enter list elements separated by space : ").split()))

    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    print("List after removing duplicates :", unique)
        






def fibonacci_series():
    print("Program : Fibonacci Series")

    print("\nCode:\n")

    print("""
n = int(input("Enter the Number of Terms : "))

a = 0
b = 1

print("Fibonacci Series :")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
""")

    print("Test Case 1")
    print("Input : 5")
    print("Expected Output : 0 1 1 2 3\n")

    print("Test Case 2")
    print("Input : 8")
    print("Expected Output : 0 1 1 2 3 5 8 13\n")

    print("Logic:")
    print("This program generates the Fibonacci series.")
    print("Each number is the sum of the previous two numbers.\n")

    print("User Execution")
    n = int(input("Enter the Number of Terms : "))

    a = 0
    b = 1

    print("Fibonacci Series :")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()






def check_even_odd():
    print("Program : Check Even or Odd")

    print("\nCode:\n")

    print("""
num = int(input("Enter a Number : "))

if num % 2 == 0:
    print(num, "is an Even Number")
else:
    print(num, "is an Odd Number")
""")

    print("Test Case 1")
    print("Input : 24")
    print("Expected Output : 24 is an Even Number\n")

    print("Test Case 2")
    print("Input : 17")
    print("Expected Output : 17 is an Odd Number\n")

    print("Logic:")
    print("This program checks whether a number is even or odd.")
    print("If the number is divisible by 2, it is even; otherwise, it is odd.\n")

    print("User Execution")
    num = int(input("Enter a Number : "))

    if num % 2 == 0:
        print(num, "is an Even Number")
    else:
        print(num, "is an Odd Number")







def find_maximum():
    print("Program : Find Maximum in a List")

    print("\nCode:\n")

    print("""
numbers = list(map(int, input("Enter list elements separated by space : ").split()))

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum Element :", maximum)
""")

    print("Test Case 1")
    print("Input : [10, 45, 23, 89, 12]")
    print("Expected Output : 89\n")

    print("Test Case 2")
    print("Input : [5, 2, 18, 7, 1]")
    print("Expected Output : 18\n")

    print("Logic:")
    print("This program finds the largest element in a list.")
    print("It compares each element with the current maximum and updates it whenever a larger value is found.\n")

    print("User Execution")
    numbers = list(map(int, input("Enter list elements separated by space : ").split()))

    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    print("Maximum Element :", maximum)





def reverse_string():
    print("Program : Reverse a String")

    print("\nCode:\n")

    print("""
text = input("Enter a String : ")

reverse = text[::-1]

print("Reversed String :", reverse)
""")

    print("Test Case 1")
    print("Input : Python")
    print("Expected Output : nohtyP\n")

    print("Test Case 2")
    print("Input : Hello World")
    print("Expected Output : dlroW olleH\n")

    print("Logic:")
    print("This program reverses a given string.")
    print("It uses Python slicing with a step of -1 to reverse the string.\n")

    print("User Execution")
    text = input("Enter a String : ")

    reverse = text[::-1]

    print("Reversed String :", reverse)









def count_case():
    print("Program : Count Uppercase and Lowercase Letters")

    print("\nCode:\n")

    print("""
text = input("Enter a String : ")

upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase Letters :", upper)
print("Lowercase Letters :", lower)
""")

    print("Test Case 1")
    print("Input : PyThOn")
    print("Expected Output : Uppercase Letters : 3")
    print("                  Lowercase Letters : 3\n")

    print("Test Case 2")
    print("Input : Hello World")
    print("Expected Output : Uppercase Letters : 2")
    print("                  Lowercase Letters : 8\n")

    print("Logic:")
    print("This program counts the number of uppercase and lowercase letters.")
    print("It checks each character using isupper() and islower() methods.\n")

    print("User Execution")
    text = input("Enter a String : ")

    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Uppercase Letters :", upper)
    print("Lowercase Letters :", lower)






def second_largest():
    print("Program : Find Second Largest Number")

    print("\nCode:\n")

    print("""
numbers = list(map(int, input("Enter list elements separated by space : ").split()))

numbers = list(set(numbers))
numbers.sort()

if len(numbers) < 2:
    print("Second largest element does not exist.")
else:
    print("Second Largest Element :", numbers[-2])
""")

    print("Test Case 1")
    print("Input : [10, 20, 30, 40, 50]")
    print("Expected Output : 40\n")

    print("Test Case 2")
    print("Input : [5, 15, 25, 15, 35]")
    print("Expected Output : 25\n")

    print("Logic:")
    print("This program finds the second largest number in a list.")
    print("It removes duplicate elements, sorts the list, and displays the second largest value.\n")

    print("User Execution")
    numbers = list(map(int, input("Enter list elements separated by space : ").split()))

    numbers = list(set(numbers))
    numbers.sort()

    if len(numbers) < 2:
        print("Second largest element does not exist.")
    else:
        print("Second Largest Element :", numbers[-2])







def simple_interest():
    print("Program : Calculate Simple Interest")

    print("\nCode:\n")

    print("""
principal = float(input("Enter Principal Amount : "))
rate = float(input("Enter Rate of Interest : "))
time = float(input("Enter Time (in years) : "))

si = (principal * rate * time) / 100

print("Simple Interest :", si)
""")

    print("Test Case 1")
    print("Input : Principal = 10000, Rate = 5, Time = 2")
    print("Expected Output : 1000.0\n")

    print("Test Case 2")
    print("Input : Principal = 5000, Rate = 8, Time = 3")
    print("Expected Output : 1200.0\n")

    print("Logic:")
    print("This program calculates the Simple Interest using the formula.")
    print("Simple Interest = (Principal × Rate × Time) / 100.\n")

    print("User Execution")
    principal = float(input("Enter Principal Amount : "))
    rate = float(input("Enter Rate of Interest : "))
    time = float(input("Enter Time (in years) : "))

    si = (principal * rate * time) / 100

    print("Simple Interest :", si)



