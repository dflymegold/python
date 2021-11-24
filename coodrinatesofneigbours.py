'''

Для клетки с координатами (x, y) в таблице размером M × N 
выведите координаты ее соседей. Соседними называются клетки, 
имеющие общую сторону.

'''
M = int(input())
N = int(input())
x = int(input())
y = int(input())
if (x!=1):
    print (x+1,y)
if (x!=M):
    print (x-1,y)
if (y!=1):
    print (x,y+1)
if (y!=N):
    print (x,y-1)