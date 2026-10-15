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


str="hello world"
print(str[1])
print(str[4])
print(str[7])
print(str[9])
print(str[3])

print(str[-3])
print(str[-4])
print(str[-9])
print(str[-5])
print(str[-11])

SLICING
print(str[1:4])
print(str[4:8])
print(str[7:11])
print(str[3:7])

print(str[0:7:3])
print(str[6:10:3])
print(str[6:12:4])
print(str[7:10:2])

str='welcome'
str2=str.capitalize()
print(str2)
print(id(str))
print(id(str2))

str3=str.isupper()
print(str3)  #return value
str4=str.lower() #convert string
print(str4)
str5=str.upper()
print(str5)
str6=str.islower()
print(str6)

print(len(str))

str7="Java is a programming language"
str8=str7.replace("Java","Python")
print(str8)

# index takes or prints the first most letter of the word where : COMUNICATION index("C ") it gives the output 0 coz it starts from first 
# rfind/rindex is also a function in which it searches the letter from last but index num is from forward and gives output 7
# if there the letter is not present in the word then it would return -1

str9="communication"
str10=str9.index("c")
print(str10)

str11=str9.rfind("c")
print(str11)

str12=""
list=['h','e','l','l','o']
str13=str12.join(list)
print(str13)

str14="welcome to python"
str15=str14.index("p",6,18)
print(str15)

# PARTITION  parts out the sentence
str16="Python is a programming language"
str17=str16.partition("is")
print(str17)

# # SPLIT   
str18="Python is a programming language"
str19=str18.split()
print(str19)

# # count
str20="i love apple ,apple is my fav fruit"
str21=str20.count("is",4,30)
print(str21)

#  printing voules
s="programming"
count=0
for ch in s:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count+=1
print(count)
