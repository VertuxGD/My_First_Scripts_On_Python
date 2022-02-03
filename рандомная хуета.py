from random import *
X = []; Y = []
for i in range(randint(10, 20)):
    i = randint(1, 50)
    if i in X:
        continue
    else:
        X.append (i)
for n in range(randint (0, len(X))):
    l = randint (0, len(X) - 1)
    if X[l] in Y:
        continue
    else:
        Y.append (X[l])
print (X); print (Y)

a = 0; b = 0
for x in range(0, len(X)):
    a += X[x]
for y in range(0, len(Y)):
    b += Y[y]
c = a * b
print (c)