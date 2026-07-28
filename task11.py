while True:
    try:
        name = input("Enter the name: ")
        weight = int(input("Enter the weight in kgs: "))
        height = float(input("Enter the height in metres: "))
        if weight > 0 and height >= 0:
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                print(f"{name} --> You are underweight as BMI is {bmi}")
            elif bmi < 25:
                print(f"{name} --> You are in Perfect shape, BMI is {bmi}")
            elif bmi < 30:
                print(f"{name} --> You are overweight, need to maintain diet, BMI is {bmi}")
            else:
                print(f"{name} --> Obesity, Your BMI is {bmi}")
            break
        else:
            print("Enter only positive values.")
    except ValueError:
        print("Invalid input. Enter integer for weight and float for height.")
    except ZeroDivisionError:
        print("Height cannot be zero.")
    finally:
        print("BMI Calculation Completed.")
