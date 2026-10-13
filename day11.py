# s1={10,20,30,40}
# s2={30,40,50,60}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s2.issubset(s1))
# print(s1.symmetric_difference(s2))

# function

# def display():
#     print("hello world")
# display()

# def add(a,b):
#     print(a+b)
# add(10,20)

# reverse
# num =int(input("enter the num:"))
# def fun(num):
#     rev=0
#     while(num>0):
#         rem=num%10
#         rev=rev*10+rem
#         num=num//10
#     return rev
# print ("reverse number : ",fun(num))


#amstrong num

num=int(input("enter the num"))
def amstron(num):
    temp=num
    rev=0
    while num>0 :
        last=num%10
        rev=rev+last**3
        num=num//10

    if temp==rev :
        print("num is amstrong")
    else:
        print("num is not amstrong")
amstron(num)