l=[10,20.3,"hello",True ,8+4j]
print(l)
print(type(l))
print(len(l))
print(id(l))

# Indexing
print(l[2])
print(l[4])

# Nested list
l1=[10,20.3,"hello",[10,20,30],["virat","rohit"],True ,8+4j]
print(l1)
print(l1[2][1])
print(l1[4][1])
print(l1[4][1][2])
print(l1[3][1])

# Slicing
a=[10,20,30,40,50,60]
# way1
print(a[:2])  
# way2
print(a[: :2])

# Reversing the list
b=(10,20,30,40,50)
print(b[::-1])

# BY USING INDEXING WE CAN ACCESS SINGLE ELEMENT AND BY USING SLICING WE USE MULTIPLE ELEMENTS

