#  2 - to reverse the given string  "python"
# s="python"
# rev=""
# for i in s :
#     rev=i+rev
# print(rev)

# s1="Hello How are you"
# s2=s1[::-1]
# print(s2)


# s5=input("enter a string:")
# word=""
# result=""
# for i in s5:
#     if i != " ":
#         word=word+i
#     else:
#         result=word + " " +result
#         word=" "
# result=word+" "+result
# print(result)


# # 4 - krishna-- output-- k/r/i/s/h/n/a
# s3=input("Enter a string:")
# for i in range(len(s3)):
#     if i<len(s3)-1:
#         print(s3[i] , end="/")
#     else:
#         print(s3[i])



# # 6 - input - python  , output- char   +veindexing    -veindexing   by using loops
# s4=input("enter a string:")
# for i in range(len(s4)):
#     print(s4[i],"  ",i,"  ",i-len(s4))


# s=input("enter a string :")
# print("char","positive index","negative index")
# for i in range(len(s)):
#     postiveindex=i
#     negativeindex=i-len(s)
#     print(s[i],postiveindex,negativeindex)



# # 7 - to check the given string is pallindrome or not . eg- s="mom"
# s6=input("enter a string :")
# rev=""
# for i in s6:
#     rev=i+rev
# if s6==rev:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")


# 8 - input- hello , output- HELLO without upper case
# s7=input("Enter a string:")
# result=""
# for i in s7:
#     if'a'<= i <= 'z':
#         result= result+chr(ord(i)-32)
#     else:
#         result=result+i
# print(result)

# 9 - input - Hello , output-hello without using lower case 
# s8=input("enter a string:")
# result=""
# for i in s8:
#     if 'A'<=i<='Z':
#         result=result+chr(ord(i)+32)
#     else:
#         result=result+i
# print(result)

# 1 - tocheck the given string is anagram or not 

# str1 = input("Enter string1: ")
# str2 = input("Enter string2: ")

# if len(str1) != len(str2):
#     print("Not Anagram")
# else:
#     for i in str1:
#         count1 = 0
#         count2 = 0

#         for j in str1:
#             if i == j:
#                 count1 += 1

#         for k in str2:
#             if i == k:
#                 count2 += 1

#         if count1 != count2:
#             print(" String is Not Anagram")
#             break
#     else:
#         print("String is Anagram")


a="silent"
b="listen"
if (sorted(a)==sorted(b)):
    print("string is anagram")
else:
    print("string is not anagram")