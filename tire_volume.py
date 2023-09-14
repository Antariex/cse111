#Import the math module
import math

#Print a description of this program to the user
print('The volume of space inside a tire can be approximated with a formula. Do it with this program!\n')

#Get the values from the user's input
user_width = float(input('Type the width of your tire in millimeters: '))
user_ratio = float(input('Type the aspect ratio of your tire: '))
user_diameter = float(input('Type the diameter in inches of your wheel: '))

#Compute the volume of space inside the user's tire
tire_volume_formula = math.pi * user_width**2 * user_ratio * (user_width * user_ratio + 2540 * user_diameter) / 10000000000

#Print the result of the formula for the user to see
print(f"The volume in liters of your tire is approximately: {tire_volume_formula:.2f}")