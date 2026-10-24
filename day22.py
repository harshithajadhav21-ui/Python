# EXCEPTION HANDLING:
# to handle the errors in multiple ways 
# IT HAVE 3 BLOCKS WHERE WE HANDLE THROUGH --- try , except , else  finally

# WITHOUT TRY - EXCEPT BLOCLK
# print("stmt-1")
# print(10/0)
# print("stmt-3")

# with try-- except block 

# print("stmt-1")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print(10/2)
# print("stmt-3")

# multiple except blocks
# try:
#     a=int(input("enter a :"))
#     b=int(input("enter b :"))
#     x=a/b
#     print(x)
# except ZeroDivisionError:
#     print("cant divide by zero")
# except ValueError:
#     print("string cant be divided by int")

# if try block have multiple blocks then it the order of these except blocks is important
try:
    x=int(input("enter x:"))
    y=int(input("enter y :"))
    a=x/y
    print(a)
except ArithmeticError:
    print("arithematic error")
except ZeroDivisionError:
    print("zero division error")