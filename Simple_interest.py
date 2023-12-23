#This is a Python program to find simple interest
# for given principal amount, time and
# rate of interest.

def simple_interest(P,T,R):
	print('The principal is', P)
	print('The time period is', T)
	print('The rate of interest is',R)
	#@AKtronics ;)
	si = (P * T * R)/100
	
	print('The Simple Interest is', si)
	return si
	
simple_interest(8, 6, 8)
