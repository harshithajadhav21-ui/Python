# # Mapping function
# # map()function executes a specified function for each item in iteration
# def sq(x):
#     return x*x
# t=(1,2,3,4,5)
# ut=map(sq,t)
# print(list(ut))

# pass statement is used for future purpose where we can keep it empty without any error for future use

# def demo():
#     pass
# demo()

# # STRING
# str1='hello'
# print(str1)

# str2="hello world"
# print(str2)

# str3='''string is the collection of the words , characters etc'''
# print(str3)


# INDEXING AND SLICING IN STRING 
# direction of +ve indexing is forward to backward 
# direction of -ve indexing is from backward to forward 


# str="hello world"
# print(str[1])
# print(str[4])
# print(str[7])
# print(str[9])
# print(str[3])

# print(str[-3])
# print(str[-4])
# print(str[-9])
# print(str[-5])
# print(str[-11])

# SLICING
# print(str[1:4])
# print(str[4:8])
# print(str[7:11])
# print(str[3:7])

# print(str[0:7:3])
# print(str[6:10:3])
# print(str[6:12:4])
# print(str[7:10:2])

str='welcome'
# str2=str.capitalize()
# print(str2)
# print(id(str))
# print(id(str2))

# str3=str.isupper()
# print(str3)  #return value
# str4=str.lower() #convert string
# print(str4)
# str5=str.upper()
# print(str5)
str6=str.islower()
print(str6)

print(len(str))

str = ""
list = ['h','e','l','l','o']
str2 = str.join(list)
print(str2)

str = "Welcome to the python"
str2 = str.index("p",19,21)
print(str2)