'''

Входные данные
Даны три целых числа, каждое записано в отдельной строке.

Выходные данные
Выведите наибольшее из данных чисел 
(программа должна вывести ровно одно целое число).
'''

number1 =int (input())
number2 =int (input())
number3 =int (input())


if (number1<number2):
    number1 = number2
if (number1<number3):
    number1 = number3
print (number1)