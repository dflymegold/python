hours1= int(input())
minutes1= int(input())
seconds1= int(input())

hours2= int(input())
minutes2= int(input())
seconds2= int(input())

secondsum1 = hours1*60*60+minutes1*60+seconds1
secondsum2 = hours2*60*60+minutes2*60+seconds2
dif = secondsum2 - secondsum1
print (dif) 