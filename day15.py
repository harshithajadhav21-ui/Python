# lamda/anonymous function
# lamda argument:expression

# greatest= lambda x,y: x if x>y else y

# print("greatest num is:",greatest(10,20))


# num=int(input("enter number:"))
# square=lambda a:a*a
# print("square num is:",square(num))

# num=int(input("enter the num"))
# numbers=lambda x:"positive number" if x>0 else "neagtive number"
# print("the number is:",numbers(num))

# num=int(input("enter num:"))
# cube=lambda b:b*b*b
# print("cube is:",cube(num))

# num=int(input("enter age"))
# age=lambda age:"elegible for vote" if age>18 else "not eleigible for voting"
# print(age(num))

# num=int(input("enter number"))
# number=lambda a:"even number" if a%2==0 else "odd number"
# print(number(num))

# num=int(input("enter marks:"))
# marks=lambda m:"Pass" if m>35 else "Fail"
# print(marks(num))



# Recursion function
# can call the same function many times

# factorial
# num=int(input("enter number:"))
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print("the factorial num is:",fact(num))


# fibbonic
n=int(input("enter number:"))
def fibonicce(n):
    if n<=1:
        return n
    return fibonicce(n-1) + fibonicce(n-2)
for i in range (n):   

    print(fibonicce(i),end="")


