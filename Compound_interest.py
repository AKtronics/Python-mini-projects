#This is a python program to find compound
#interest for input taking from user.

def compound_interest(principal, rate, time):

	# Calculates compound interest
  
	Amount = principal * (pow((1 + rate / 100), time))
	Ci = Amount - principal
  #@AKtronics ;)
	print("Compound interest is", Ci)
  return Ci

#Taking input from user.

Principal = int(input("Enter the principal amount: "))
Rate = int(input("Enter rate of interest: "))
Time = int(input("Enter time in years: " ))

#Function Call

compound_interest(Principal,Rate,Time)

