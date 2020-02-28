import random
inptim=1
while(inptim<=5):
#getting 5 times input
  ran=int(input("Guess the integer between 0 to 20:"))
#Assigning system generated randam number
  ran_num = random.randint(0, 20)
  print(ran_num)
#Checking the user input and randam number
  if(ran==ran_num):
    print("You Guessed it right!")
    break
  elif(ran<ran_num):
    print("Your guess is a little low")
else:
  print("Your guess is higher")
inptim=inptim+1