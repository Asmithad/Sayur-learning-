#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input. The chart below shows the range. http://www.milkaclarkestrokefoundation.org/uploads/2/4/5/9/2459046/bmi-index_orig.jpg Use logical and/or conditions.

#Code:

# Get user input for weight in kilograms and height in meters
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI (Body Mass Index)
bmi = weight / (height ** 2)
print("BMI: ", bmi)

# Determine weight status based on BMI
if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 24.9:
    status = "Normal weight"
elif 25 <= bmi < 29.9:
    status = "Overweight"
else:
    status = "Obese"

# Display the weight status
print("Weight Status: ", status)



