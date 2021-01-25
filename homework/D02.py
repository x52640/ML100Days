import numpy as np

array1 = np.array(range(30))
array2 = array1.reshape((5,6),order='F')
print(array2)
print(np.where(array2%6 == 1))
