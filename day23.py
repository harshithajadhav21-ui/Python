# if we dont have any error in try then only else block execute

# class tooyoungexception(Exception):
#     def _init_ (self,arg):
#         self.msg=arg

# class tooldexception(Exception):
#     def __init__(self, arg):
#         self.msg=arg

# age=int(input("enter age:"))
# if age>40:
#     raise tooldexception("your age is exceed for marriage")
# elif age<18:
#     raise tooyoungexception("your age is too young for marriage")
        
# else:
#     print("marriage")




# DECORATORS:
# adding new functionality without removing the existing functionality
# it checks ravi == ravi then only the condition gets satisfied

# def decor(func):
#     def inner(name):
#         if name=="ravi":
#             print ("hello",name,"bad morning")
#         else:
#             func(name)
#     return inner

# @decor
# def wish(name):
#     print("hello",name,"good morning")
# wish("harsh")
# wish("hima")
# wish("ravi")

# 10 examples on exception handling 
# 5 examples on decorators

# WITHOUT USING DECOR FUNCT
def decor(func):
    def inner(names):

        if names =="adi":
           print("hello",names,"bad morning")
        else:
           func(names)
    return inner

def wish(names):
    print("hello",names,"good morning")
decorfunction=decor(wish)

wish("durga")
wish("adi")
decorfunction("durga")
decorfunction("adi")
