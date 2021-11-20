'''
Длина Московской кольцевой автомобильной дороги —109 километров. 
Байкер Вася стартует с нулевого километра МКАД и едет со скоростью v километров в час. 
На какой отметке он остановится через t часов?

Входные данные
Программа получает на вход значения v и t. 
Если v>0, то Вася движется в положительном направлении по МКАД, если же значение v<0, то в отрицательном.

Выходные данные
Программа должна вывести целое число от 0 до 108 — номер отметки, на которой остановится Вася.

'''

v = int (input ())
t = int (input())

rez = ((v*t)%109+109)%109
print (rez)
