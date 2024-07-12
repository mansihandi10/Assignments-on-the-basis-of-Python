# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:38:22 2024

@author: Hp
"""

'''Write a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o, or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise, your program should display a message indicating that the
letter is a consonant
'''

def identify_letter(letter):
    # Convert letter to lowercase to make the function case-insensitive
    letter = letter.lower()
    
    if letter in ('a', 'e', 'i', 'o', 'u'):
        print(f"{letter} is a vowel")
    elif letter == 'y':
        print(f"{letter} is sometimes used as a vowel and sometimes as a consonant.")
    else:
        print(f"{letter} is a consonant")

# Get user input
letter = input("Enter any letter: ")

# Validate the input
if len(letter) == 1:
    identify_letter(letter)
   
else:
    print("Please enter a single letter.")
    
    
'''Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If several sides outside of this range are entered
then your program should display an appropriate error message.
'''

def shape(num_sides):


    # Determine the shape or display an error
    if num_sides == 3:
        print("A shape with 3 sides is a Triangle.")
    elif num_sides == 4:
        print("A shape with 4 sides is a Quadrilateral.")
    elif num_sides == 5:
        print("A shape with 5 sides is a Pentagon.")
    elif num_sides == 6:
        print("A shape with 6 sides is a Hexagon.")
    elif num_sides == 7:
        print("A shape with 7 sides is a Heptagon.")
    elif num_sides == 8:
        print("A shape with 8 sides is an Octagon.")
    elif num_sides == 9:
        print("A shape with 9 sides is a Nonagon.")
    elif num_sides == 10:
        print("A shape with 10 sides is a Decagon.")
    else:
        print("Error: Please enter a number between 3 and 10.")


num_sides = int(input("Enter the number of sides:"))
shape(num_sides)

'''The length of a month varies from 28 to 31 days. In this exercise, you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.'''
def month(month_name):
# Ask the user to input the name of the month
     # Convert to lowercase for easier comparison
    
    # Determine the number of days in the month
    if month_name == "february":
        print("28 or 29 days")
    elif month_name in ("april", "june", "september", "november"):
        print("30 days")
    elif month_name in ("january", "march", "may", "july", "august", "october", "december"):
        print("31 days")
    else:
        print("Invalid month name")
    
month_name = input("Enter the name of a month: ").lower()        
month(month_name)

'''A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.
'''
def traingle(s1,s2,s3):
    
    
    if (s1==s2==s3):
        print("Traingle is Equilateral")
    elif (s1==s2) or (s2==s3) or (s3==s1):
        print("Traingle is isosceles")    
    else:
        print("Tringle consist of three different sides. ")

s1=int(input("Enter the side 1: "))
s2=int(input("Enter the side 2: "))
s3=int(input("Enter the side 3: "))        
traingle(s1,s2,s3)    

'''The year is divided into three seasons: summer, rainy, and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
the way that the calendar is constructed, Write a program to display the season if the date is given.
'''