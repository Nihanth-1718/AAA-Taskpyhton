n = int(input("Enter number of rows: "))

print("\nPattern 4")

# Upper Part
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Lower Part
for i in range(n - 1, 0, -1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
