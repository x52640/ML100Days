import numpy as np

array1 = np.array(range(30))
array2 = np.array([2, 3, 5])

with open('D06.npz', 'wb') as f:
    np.savez(f, a = array1, b =array2)

array3 = np.array(range(5))
npzfile = np.load('D06.npz')
print(npzfile.files)

with open('D06.npz', 'wb') as f:
    np.savez(f, a = array1, b = array2, c = array3)

npzfile2 = np.load('D06.npz')
print(npzfile2.files)

for i in npzfile2.files:
    print(npzfile2[i])