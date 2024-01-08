print("Welcome BMI Calculator")

weight = int(input("Your weight(kg): "))
height = float(input("Your height(m): "))

bmi = weight / height ** 2

print(f"Your BMI: {bmi}")

if bmi < 18.5:
    print("Result: Underweight ")
elif 18.5 < bmi < 25:
    print("Result: Normal weight")
elif 25 < bmi < 30:
    print("Result: Overweight")
elif bmi > 30:
    print("Result: Obese")
else:
    print("Try again")
