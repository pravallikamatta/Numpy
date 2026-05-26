import numpy as np 
array = np.array([1,2,3])
print(array.ndim)

newarr=np.arange(1,10)##st stop anddd step
print(newarr)

arr=np.ones([3,4],dtype=int)

f_arr=np.full([2,4],7)
print(f_arr)

##contains garbage/uninitialized values initially
A=np.empty((2,3))
print(A)