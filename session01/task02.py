name = input("Input Name: ")
weight = float(input("Input Weight (KG): "))
height = float(input("Input Height (CM): "))


bmi = round(weight / (height / 100) ** 2, 1)

bmi_status = "OBESE"

if bmi <= 18.5:
    bmi_status = "UNDERWEIGHT"
elif bmi > 18.5 and bmi <= 24.9:
    bmi_status = "UNDERWEIGHT"
elif bmi > 24.9 and bmi <= 29.9:
    bmi_status = "OVERWEIGHT"


print(f"Your BMI value is '{bmi}' and you are : '{bmi_status}'")
