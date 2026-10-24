# numpy is only for array

# import numpy as np
# arr=np.array([1,2,3,4])
# print(arr)

# import numpy
# arr=numpy.array([1,2,3,4])
# print(arr)

# types of array: 1D-- VECTOR  2D--SCALAR MULTI-D-- TENSOR
# import numpy as np
# arr0=np.array(21)
# arr1=np.array([1,23,3,4])
# arr2=np.array([[1,2],[4,5]])
# arr3=np.array([[12,4],[2,3],[4,5]])
# print(arr2)


# 4bytes -- 64
#  2bytes -- 32
# import numpy as i
# arr1=i.array([1,2,3])
# print(arr1.dtype)

# import numpy as i
# arr2=i.array([1.34,2.56,3.43])
# print(arr2.dtype)

# import numpy as i
# arr3=i.array(['char','harsh'])
# print(arr3.dtype)


# import numpy as comp
# x=comp.array([3,5])
# y=comp.array([2,5])
# print("orignal numbers :-")
# print(x)
# print(y)
# print("comparision")
# print(comp.greater(x,y))
# print("comaprision greater_equal")
# print(comp.greater_equal(x,y))
# print("comparision less")
# print(comp.less(x,y))
# print("comparision_less_equal")
# print(comp.less_equal(x,y))

# import numpy as row
# a=row.array([11,12,13,14,15,16,17,18,19,20 , 21,22])
# # 1D ARRAY
# na=a.reshape(4,3)
# print(na)

# # 2D ARRAY
# naa=a.reshape(2,2,3)
# print(naa)

# for x in a:
#     print(x)

# import numpy as np
# a=np.array([[1,2,3,4],[5,6,7,8]])

# for i in a:
#     print(i)
# for i in np.nditer(a):
#     print(i)

# b=np.array([1,2,3,4,5,6,7,8])
# n=np.where(a==4)
# print(n)

import numpy as np
a=np.array([1,5,3,8,5,9,7])
x=np.where(a%2==0)
print(x)

print(np.sort(a))