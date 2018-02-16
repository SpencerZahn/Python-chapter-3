#Spencer Zahn - Python lesson 2 - Chapter 3 - Exercise 1 - 013118

# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0
 
y = float(input("Enter Rate: "))
x = float(input("Enter time worked: "))
if x > 40:
        z = y * x * 1.5 - 200
else:
        z = y * x
print ("Pay: " + str(z))
