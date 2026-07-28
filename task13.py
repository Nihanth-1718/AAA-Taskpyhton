bmi_database = {
    "person_name": [],
    "bmi_score": []
}

def calculate_bmi(**person_details):

    bmi_value = person_details["weight"] / (person_details["height"] ** 2)
    bmi_value = round(bmi_value, 2)

    bmi_database["person_name"].append(person_details["name"])
    bmi_database["bmi_score"].append(bmi_value)

    if bmi_value < 18.5:
        print(f'{person_details["name"]} --> You are Underweight as BMI is {bmi_value}')
    elif bmi_value < 25:
        print(f'{person_details["name"]} --> You are in Perfect shape, BMI is {bmi_value}')
    elif bmi_value < 30:
        print(f'{person_details["name"]} --> You are Overweight, need to maintain diet, BMI is {bmi_value}')
    else:
        print(f'{person_details["name"]} --> Obesity, Your BMI is {bmi_value}')


while True:
    try:
        total_people = int(input("Enter the number of users: "))
        if total_people > 0:
            break
        else:
            print("Enter a positive number.")
    except ValueError:
        print("Invalid input.")

for person_index in range(total_people):

    while True:
        try:
            person_name = input("Enter the Name: ").strip()
            person_weight = float(input("Enter the weight in kgs: "))

            height_unit = input("Enter height unit (cm/feet/inches): ").lower()

            if height_unit == "cm":
                person_height = float(input("Enter the height in cm: "))
                person_height /= 100

            elif height_unit == "feet":
                person_height = float(input("Enter the height in feet: "))
                person_height *= 0.3048

            elif height_unit == "inches":
                person_height = float(input("Enter the height in inches: "))
                person_height *= 0.0254

            else:
                print("Invalid unit.")
                continue

            if person_weight > 0 and person_height > 0:
                break
            else:
                print("Weight and height must be positive.")

        except ValueError:
            print("Invalid input.")

    calculate_bmi(
        name=person_name,
        weight=person_weight,
        height=person_height
    )

print("\nStored BMI Details")
print(bmi_database)
