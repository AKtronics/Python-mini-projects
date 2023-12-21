#This is a python program for checking if an array is a palindrome or not.

#A palindrome is a sequence which when reversed is same as the original one.

def Palindrome(arr) :
    rra = arr[ : :-1]
#@AKashtronics ;)    
    if arr == rra :
      print("YES the array is a palindrome ")
    else :
      print("NO the array is not a palindrome")
      
      
#Test cases
      
Palindrome("121")
Palindrome((4,5,4))
Palindrome ([1,2,3])

