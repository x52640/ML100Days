import numpy as np

array1 = np.array([[10, 8], [3, 5]])
i = np.linalg.inv(array1)
print(np.dot(array1, i))

w, v = np.linalg.eig(array1)
print(w)
print(v)

u, s, vh = np.linalg.svd(array1)
print(u)
print(s)
print(vh)