'''
На сковородку одновременно можно положить k котлет.
 Каждую котлету нужно с каждой стороны обжаривать m минут непрерывно.
 За какое наименьшее время удастся поджарить с обеих сторон n котлет?

Входные данные
Вводятся 3 числа: k, m и n. Все числа не превосходят 32000.

Выходные данные
Вывести время, за которое все котлеты будут обжарены.

'''


k = int (input())
m = int (input())
n = int (input())
if n<k :
    time =2*k
elif n*2%k == 0 : 
    time = m*(n*2//k)
else :
    time = m*(1+(n*2//k))
print (time)
