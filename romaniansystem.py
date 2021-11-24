'''
Дано число X. Требуется перевести это число в римскую систему счисления.

Входные данные
Дано число X в десятичной системе счисления (1  ≤  X  ≤  100).

Выходные данные
Выведите X в римской системе счисления.

'''

X = int (input())
X1 =X%10
X2 = X//10
if X2 == 1 :
    print ("X")
if X2 == 2 :
    print ("XX")
if X2 == 3 :
    print ("XXX")
if X2 == 4 :
    print ("XL")
if X2 == 5 :
    print ("L")
if X2 == 6 :
    print ("LX")
if X2 == 7 :
    print ("LXX")
if X2 == 8 :
    print ("LXX")
if X2 == 9 :
    print ("XC")
if X2 == 10 :
    print ("C")

if X1 == 1 :
    print ("I")
if X1 == 2 :
    print ("II")
if X1 == 3 :
    print ("III")
if X1 == 4 :
    print ("IV")
if X1 == 5 :
    print ("V")
if X1 == 6 :
    print ("VI")
if X1 == 7 :
    print ("VII")
if X1 == 8 :
    print ("VIII")
if X1 == 9 :
    print ("XIX")