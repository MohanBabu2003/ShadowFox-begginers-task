def calculate_bmi(height, weight):
    return weight / (height ** 2)

def determine_bmi_category(bmi):
    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = calculate_bmi(height, weight)
category = determine_bmi_category(bmi)
print(category)
