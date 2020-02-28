places = ['Guindy','Ramapuram','Tambaram','Porur','Tharamani','Vadapalni']
mode=['Bike','Auto','Mini','Micro','Prime','seedan']
fare=[10,20,30,40,50,60]
#Display the available places
for i in range(0,len(places)):
 print(str(int(i)+1)+"."+places[i])
#Get the input Source 
sorval= int(input("Select From:"))
#Get the Destination
desval=int(input("select Destination:"))
#Get vehicle mode
for j in range(0,len(mode)):
   print(str(int(j)+1)+"."+mode[j])
modinp=int(input("Select Vehicle Mode:"))
#check for valid option
if(sorval>((len(places))+1))or sorval<1 or(desval>((len(places))+1)) or desval<1 or (modinp>((len(mode))+1))or modinp<1:
  print()
  print("RESULT")
  print("------")
  print("Not a valid option")
else:  
 sour=places[sorval-1]
 dest=places[desval-1]
 veh=mode[modinp-1]
 print()
 print("COST")
 print("----")
 #Assign Cost
 print("Raid Cost from "+sour+" to" +dest+" was RS:"+str(fare[modinp-1]))