# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_as_int = float(weight)
height_as_int = float(height)
BMI=weight_as_int/(height_as_int)**2
print(int(BMI))
