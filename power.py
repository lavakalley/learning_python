
#This program is for if else statement will print different letters based on number entered
score = int(input("Enter any number ?"))

if score >= 90:
    letter = 'A'
elif score >= 80:
    letter = 'B'
elif score >= 70:
    letter = 'C'
elif score >= 60:
    letter = 'D'
else:
    letter = 'F'

print (letter)
