a = int (input())
b = int (input())
c = int (input())
d = int (input())

if a == 0 or b == 0 :
    print ("INF")
elif a == 0 or b*c == a * d :
    print ("NO")
elif b%a == 0 :
    print (-b//a)
else :
    print ("NO")