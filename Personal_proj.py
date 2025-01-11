# Making a simple Body Mass Index (BMI) Calculator

# Taking input from the user
weight = float(input("Enter your weight in kilograms: "))
feet = float(input("Enter your height in feet: "))
inches = float(input("Enter your height in inches: "))

# Converting to meters
height_final = (feet * 0.3048) + (inches * 0.0254)

# Calculating BMI
BMI = weight / (height_final**2)
if height_final < 0:
    print("Invalid Height!")
else:
    print(f"Your Body Mass Index is {BMI:.3f}")

# Specifying condition
if BMI < 18.5:
     print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("You have a normal weight.")
elif 25 <= BMI < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
