# This is a python program for finding the roots of any quadratic equation.
import math

# Input coefficients

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant

discriminant = (b ** 2) - (4 * a * c)

# Check if the discriminant is positive, negative, or zero

if discriminant > 0:
  
  # Two real and distinct roots
  
  root1 = (-b + math.sqrt(discriminant)) / (2*a)
  root2 = (-b - math.sqrt(discriminant)) / (2*a)
  print("Root 1: ",root1)
  print("Root 2: ",root2)
  #@AKtronics ;)
elif discriminant == 0:
  
 # One real root (repeated)
  
 root = -b / (2 * a)
 print("Root: ",root)
  
else:
  
 # Complex roots
  
 real_part = -b / (2 * a)
 imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
 print("Root 1: ",real_part," + ",imaginary_part,"i")
 print("Root 2: ",real_part, " - ",imaginary_part,"i")
