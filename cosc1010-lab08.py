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
        int(strings)
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
    
    if ((m_num or m_num == 0) and
        (b_num or b_num == 0) and
        (xl_num or xl_num == 0) and
        (xu_num or xu_num == 0)):
            y_arr = []
    for x in range(xl_num, xu_num + 1):
        y = m_num * x + b_num

print(point(2,2,2,2))






# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

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
