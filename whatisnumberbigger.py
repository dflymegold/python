'''
Входные данные
Даны два целых числа, каждое записано в отдельной строке.

Выходные данные
Программа должна вывести число 1, если первое число больше второго, 
число 2, если второе больше первого, или число 0, если они равны.

'''

number1 =int(input())
number2 = int (input())
if number1 >number2 :
    print (number1)
elif number2 >number1 :
    print (number2)
elif number1 == number2 :
    print (0)