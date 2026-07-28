BMI_results = {
    "name": [],
    "BMI_values": []
}
n = int(input("Enter the number of users: "))
for i in range(n):
    name = input("Enter the name: ")
    weight = float(input("Enter the weight (kg): "))
    print("Choose height unit")
    print("1. Inches")
    print("2. Centimetres")
    print("3. Feet")
    choice = int(input("Enter your choice: "))
    height = float(input("Enter the height: "))
    if choice == 1:
        height = height * 0.0254
    elif choice == 2:
        height = height / 100
    elif choice == 3:
        height = height * 0.3048
    else:
        print("Invalid choice")
        continue
    bmi = weight / (height ** 2)
    BMI_results["name"].append(name)
    BMI_results["BMI_values"].append(round(bmi, 2))
    if bmi < 18.5:
        print(f"{name} --> Underweight, BMI = {round(bmi,2)}")
    elif bmi < 25:
        print(f"{name} --> Normal Weight, BMI = {round(bmi,2)}")
    elif bmi < 30:
        print(f"{name} --> Overweight, BMI = {round(bmi,2)}")
    else:
        print(f"{name} --> Obesity, BMI = {round(bmi,2)}")
print("\nBMI Results Dictionary")
print(BMI_results)
