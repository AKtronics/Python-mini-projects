#This is a python program for a small game of guessing a number
#rules: you enter an intger of your choice from 0 to 10, if it is the same number the computer takes, you win.

import random
x = random.randint(0,10)
count = 0

#__main__

while True:
    
  choice = int(input("Choose a number between 0 and 10:"))
  
  if choice >= 0 and choice <= 10:
      
      if x == choice:
          count+=1
          
          if count == 1:
              print("Comgratulations you guessed it right in ",count," try!")
          #@Aktronics ;)    
          else:
              print("Comgratulations you guessed it right in ",count," tries!")
          break    
      
      else:
          count+=1
          print("Your guess was wrong! try once again.")
          print(" ")
          
  else:
      print("Invalid Choice!")
