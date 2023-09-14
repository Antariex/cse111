#Print a description of this program to the user
print('This program will help you discover the target heart rate to strengthen your heart\n')

#Get the user's age as input
user_age = int(input('Please enter your age: '))

#Calculate the target heart rate range
max_rate = 220 - user_age
slowest = max_rate * 0.65
fastest = max_rate * 0.85

#Print the result for the user to see
print(f'When you exercise to strengthen your heart, you should keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.')