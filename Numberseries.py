1)
#get the input as range from user
inp_ran=int(input("Enter the range:"))
ans=0
for i in range(1,inp_ran+1):
  ans=ans+int(i)
print (ans)



ii)

#get the input as range from user
inp_ran=int(input("Enter the range:"))
fir=1
sec=2
print(fir,end=" ")
print(sec,end=" ")
for i in range(3,inp_ran+1):
  if(i%2!=0):
    ans1=fir+sec
    print (ans1,end=" ")
    thi=ans1 
  else:
    ans1=fir+sec+thi
    print(ans1,end=" ")
    fir=thi
    sec=ans1

iii)

inp_ran=int(input("Enter the range:"))
for i in range(1,inp_ran+1):
  print(str(i**2),end=" ")

iv)


inp_ran=int(input("Enter the range:"))
for i in range(1,inp_ran+1): 
 if(i%2!=0):
   print (str(i**2),end=" ") 
 else: 
  print(i ,end=" ") 

V)


#get the input as range from user

inp_ran=int(input("Enter the range:"))
fir=1
sec=5
print(fir,end=" ")
print(sec,end=" ")
for i in range(3,inp_ran+1): 
 if(i%2!=0): 
  print (str(i**2),end=" ") 
 else: 
  sec=sec+fir
  print (str(sec),end=" ")
  fir=fir+1

vi)

inp_ran=int(input("Enter the range:"))
for i in range(1,inp_ran+1): 
 if(i%2!=0): 
  print (str(i**3),end=" ") 
 else: 
  print (str(i**2),end=" ")


v)


#get the input as range from user
inp_ran=int(input("Enter the range:"))
fir=1
sec=0
for i in range(1,inp_ran+1): 
 if(i%2!=0): 
  print (str(i**2),end=" ") 
else: 
  print (str(2*2+(fir)),end=" ") 
  sec=sec+1
  fir=fir+sec

ii)


#get the input as range from user

inp_ran=int(input("Enter the range:"))
fir=1
print(fir,end=" ")
for i in range(1,inp_ran+1): 
 if(i%2!=0): 
  ans1=fir*2
  print (ans1,end=" ") 
  fir=ans1
 else: 
  sec=fir*0.5
  ans1=int(sec)+fir 
  print (ans1,end=" ") 
  fir=ans1