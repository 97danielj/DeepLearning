import numpy as np
from numpy.linalg import inv


A = np.arange(1,10).reshape(3,3)
print(A)
print(inv(A))

X=np.array([[2,3],[1,-2]])
Y=np.array([[1],[4]])
inv_X = inv(X)

print(inv_X.shape)
print(Y.shape)
W=inv_X.dot(Y)
print(W)

