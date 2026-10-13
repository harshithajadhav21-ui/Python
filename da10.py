# LIST AND TUPLES
# l1=[1,2,3]
# l2=[4,5,6]
# print(l1+l2)
# print(l1*2)
# print(l1[0])
# print(l1[0:2])

# fruits=["apple","banana","cherry"]
# fruits.append("orange")
# print(fruits)

# a=["apple","orange","kiwi"]
# b=["banana","cherry"]
# a.append(b)
# print(a)

# fruits.clear()
# print(fruits)

# x=fruits.copy()
# print(x)

# y=fruits.count("cherry")
# print(y)

# z=fruits.index("cherry")
# print(z)

# fruits=[2,3,55,3,2,9]
# a=fruits.index(55)
# print(a)

# fruits=["apple","banana","cherry"]
# fruits.insert(1,"jackfruit")
# print(fruits)

# fruits.pop(2)
# print(fruits)

# fruits.reverse()
# print(fruits)


# fruits.sort()
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)

# TUPLE
# not mutable 
# once defined cant be changed
# readonly 

# t=(1,2,3)
# print(t)
# t[2]=3
# print(t)

# l=(10,20,"hi",3+1j)
# print(l)

# t1=(1,2,3,4)
# print(sum(t1))
# print(len(t1))
# print(min(t1))
# print(max(t1))
# print(reversed(t1))



# DAY 11
# hold key and valu pair
# it is mutable
# it is like a assosivative array or hash table where each keys 
# stores as a specific value 

# D={1:"python",2:"java"}
# print(D)

# d1={}
# print(type(d1))

# s={}
# print(type(s))


# d={1:101,"a":102}
# print(d)
# print(d.keys())
# print(d.values())

# mydict={"id":101,"name":"harsh","age":21}
# v=mydict.get("name")
# print(v)

# c=mydict.copy
# print(c)

# mydict={"id":101,"name":"harsh","age":21}
# mydict.pop("age")
# print(mydict)

# names={1:"pune",2:"sangli",3:"satara",4:"mumbai"}
# print(sorted(names.keys()))
# print(sorted(names.items()))

# mydict={"id":101,"name":"harsh","age":21}
# i=mydict.items()
# print(i)
# mydict.update({"city":"sangli"})
# print(mydict)
# mydict.setdefault("city","pune")
# print(mydict)
# mydict["city"]="sangli"
# print(mydict)

# SET
# un ordered collection of unique elements
# sets are mutable
# it may return  to the changed sequence ofthe element
# indexing or slicing are nog applicable

# s={2,3,4,5,6,7,2,5,8}
# print(s)

# set1=set()
# set2={'abc',2,4,'xyz'}
# print(set2)
# set2.add(10)              '''add for single element'''
# print(set2)
# set2.remove(2)
# print(set2)

flowers={"rose","lily","lotus"}
flowers.pop()
print(flowers)

a={"rose","lily","lotus"}
b={"python","c","sql"}
# a.update(b)                        
# print(a)

c=a.union(b)
print(c)

