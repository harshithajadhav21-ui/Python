# 1 - tocheck the given string is anagram or not 
# 2 - to reverse the given string  "python"
# 3 - "Hello how are you "   , "krishna"
# 4 - krishna-- output-- k/r/i/s/h/n/a
# 5 - count a frequency of givan string - programming p-1 r-2 o-1 g-1
# 6 - input - python  , output- char   +veindexing    -veindexing   by using loops
# 7 - to check the given string is pallindrome or not . eg- s="mom"
# 8 - input- hello , output- HELLO without upper case
# 9 - input - Hello , output-hello without using lower case 

s1="mom"
s2=s1[::-1]
if(s1==s2):
    print("string is pallindrome ")
else:
    print("string is not a pallindrome")


# ARRAYS
# proper array dont support python where therfore it uses list
# d for float integer
from array import*
a=array('i',[2,4,6,8])
print(a)

import array as arr
a=arr.array('i',[2,4,6,8])
print(a)

# ADD ELEMENT
import array as arr
num=arr.array('i',[2,4,6,8])
num[0]=0
print(num)

import array as arr
num= arr.array('i',[1,2,3,4,5])
num[2:5]=arr.array('i',[4,6,8])
print(num)

# delete element
import array as arr
num= arr.array('i',[1,2,3,4,5])
del num[2]
print(num)

# Concadation
import array as arr
a=arr.array('d',[1.0,2.0,3.0,4.0,5.0])
b=arr.array('d',[2.1,3.1])
c=arr.array('d')
c=a+b
print("C=",c)