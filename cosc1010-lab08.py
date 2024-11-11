# Gabrial Escajeda
# UWYO COSC 1010
# 11/4/24
# Lab 08
# Lab Section: 14
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def hehe(strings):
    returnvalue = False
    try:
        returnvalue = float(strings)
        return returnvalue
    except:
        return returnvalue

print(hehe("-57"))

print("*" * 75)

# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

def point(m,b,xl,xu):
    m_num = hehe(m)
    b_num = hehe(b)
    xl_num = hehe(xl)
    xu_num = hehe(xu)
    
    xl_num = int(xl_num) if isinstance(xl_num, (int)) else False
    xu_num = int(xu_num) if isinstance(xu_num, (int)) else False

    if isinstance(m_num, (int, float)) and isinstance(b_num, (int, float)) and isinstance(xl_num, (int, float)) and isinstance(xu_num, (int, float)):
        if xl_num > xu_num:
            return False
        y_arr = []
        for x in range(xl_num, xu_num + 1):
            y = m_num * x + b_num
            y_arr.append(y)
        return y_arr
    else:
        return False

print(point(2,2,2,2))


# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

while True:
    m = input("Enter the slope or 'exit' to quit (mx + b): ")
    if m.lower() == "exit":
        break
    b = input("Enter the y-intercept or 'exit' to quit: ")
    if b.lower() == "exit":
        break
    xl = input("Enter the lower bound for x or 'exit' to quit: ")
    if xl.lower() == "exit":
        break
    xu = input("Enter the upper bound for x or 'exit' to quit: ")
    if xu.lower() == "exit":
        break

    resulting_list = point(m,b,xl,xu)
    if resulting_list:
        print("The resulting list of Y values is:", resulting_list)
    else:
         print("There was an error with the numbers entered.")

print("*" * 75)

# Use fuction from part 1 here
# Function keeps looping until user types exit
# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

import math

def squareR(number):
    if number < 0:
        return None
    return math.sqrt(number)

def quadratic(a, b, c):
    inside = b**2 - 4*a*c

    if inside < 0:
        return None

    Kinda_Answer = squareR(inside)
    if Kinda_Answer is None:
        return None

    root1 = (-b + Kinda_Answer) / (2*a)
    root2 = (-b - Kinda_Answer) / (2*a)
    
    return root1, root2

while True:
    a = input("Enter the value for a or type 'exit' to quit (quadratic formula): ")
    if a.lower() == "exit":
        break
    b = input("Enter the value for b or type 'exit' to quit: ")
    if b.lower() == "exit":
        break
    c = input("Enter the value for c or type 'exit' to quit: ")
    if c.lower() == "exit":
        break
    
    a_num = hehe(a)
    b_num = hehe(b)
    c_num = hehe(c)

    if isinstance(a_num, (int, float)) and isinstance(b_num, (int, float)) and isinstance(c_num, (int, float)):
        result = quadratic(a_num, b_num, c_num)
        if result is None:
            print("No real solutions (discriminant is negative).")
        else:
            print(f"The solutions are: {result[0]} and {result[1]}")
    else:
        print("Invalid input. Please enter valid numbers.")