# num=int(input("enter a num"))
# rev=0
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print("Reverse numis",rev)

# PALINDROME
# num=int(input("enter num"))
# rev=0
# temp=num
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print("reverse num is",rev)
# if(temp==rev):
#         print("the num is palindrome")
# else:
#         print("the num is not palindrome")


# AMSTRONG NUM:
# the number given have 3digit , 2 digit or whtaever then when we do its cube square if we have 3 digit num wewant to
# do the cube , if 2 num then square like that we do the amstong num where when we do cube or square the total num comes 
# should be the same as the number given 
# num= int (input("enter the num"))
# sum=0
# temp=num
# while(num>0):
#        rem=num%10
#        sum=sum+rem**3
#        num=num//10
# print("the reversenum is:",sum)
# if(temp==sum):
#        print("the num is amstrong")
# else:
#        print("the num is not amstrong")

# num=int(input("enter the num"))
# sum=0
# while(num>0):
#     rem=num%10
#     sum=sum+rem
#     num=num//10
# print("sum is:",sum)


num=int(input("enter the num"))
mul=1
while(num>0):
    rem=num%10
    mul=mul*rem
    num=num//10
print("multiplication is:",mul)
