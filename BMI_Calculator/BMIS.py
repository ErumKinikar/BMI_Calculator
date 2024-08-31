print("Welcome to the BMI Calculator!")
print("This program will calculate your Body Mass Index (BMI) and determine your weight category.\n")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

BMI = (weight)/(height*height)

for bmi_value, result in [(18, 'The person is: Underweight'), 
                          (24.9, 'The person is: Normal'), 
                          (30, 'The person is: Overweight')]:
    if BMI <= bmi_value:
        print(f"\nYour BMI is: {BMI:.2f}")
        print(result)
        break
else:
    print(f"\nYour BMI is: {BMI:.2f}")
    print("The person is: Obese")
