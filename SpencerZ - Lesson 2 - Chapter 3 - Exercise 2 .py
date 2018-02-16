#Spencer Zahn - Python lesson 2 - Chapter 3 - Exercise 2 - 013118

#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

try:
    x = float(input("Enter Hours: "))
    y = float(input("Enter Rate: "))
    z = x * y

    print ("Pay: " + str(z))

except:
    print ("Error, please enter numeric input")
