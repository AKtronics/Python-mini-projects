#This is a python program to check whether a number is Armstrong number or not.

#It is a number that is equal to the sum of its own digits, each raised to a power equal to the
#number of digits in the number.
#For example, let's consider the number #153:
#It has three digits (1, 5, and 3).
#If we calculate + , we get , which is equal to .

num = int(input("Enter a number: "))

# Calculate the number of digits in num

num_str = str(num)
num_digits = len(num_str)

# Initialize variables

sum_of_powers = 0
temp_num = num
#@AKtronics
# Calculate the sum of digits raised to the power of num_digits

while temp_num > 0:
 digit = temp_num % 10
 sum_of_powers += digit ** num_digits
 temp_num //= 10

# Check if it's an Armstrong number

if sum_of_powers == num:
 print(num," is an Armstrong number.")
else:
 print(num," is not an Armstrong number.")
