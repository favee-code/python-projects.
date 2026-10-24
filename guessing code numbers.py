import random


secret=random.randint(1, 100)
tries = 0


 print( " i'm thinking of a number between 1 and 100.")


   while true:
       guess= int(input( "your guess:  ") )


       if guess < secret:
           print ("Too low! " )
           elif guess > secret:
             print (" too high" )
           else:
               print(f"correct! you got it in {tries} tries." )
               break
