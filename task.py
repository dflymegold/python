# f(X)= A*X^3+B*X^2+C*X+D
A = [3.1,2.1,1.6]
B = [10.3,8.8,0.2]
C = [-2.8,-11.4,-20.8]
D = [10.3,-5.6,38.5]
X = [-4,-3,-2,-1,0,1]
REZ = []
for i in range (0,len(A)) :
    for j in range (0,len(X)) :
        k = A[i]*X[j]*X[j]*X[j]+B[i]*X[j]*X[j]+C[i]*X[j]+D[i]
        REZ.append(k)
maximum = max (REZ)
minimum = min (REZ)
print (maximum,minimum)
