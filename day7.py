# for i in range (1,10):
#     print (i)

# for i in range (1,10,2):
#     print(i)


# for i in range (1,11):
#     print (i,"square is =",i*i)

# for i in range (1,11):
#     print(i,"cube is",i*i*i)

# for i in range(1,10):
#     if(i%2==0):
#         print(i)

# for i in range(1,10):
#     if(i%2!=0):
#         print(i)

# num= int(input("enter num"))
# sum=0
# for num in range(1,num+1):
#     sum = sum+num
# print(sum)

# num=int(input("enter num"))
# sum=0
# for i in range(2,num+1):
#     if i%2==0 :
#         sum=sum+i
# print(sum)

# num =int (input("enter n"))
# sum=0
# for r in range(2,num+1):
#     if r%2!=0:
#         sum=sum+r
# print(sum)

# num=int(input("enter num"))
# for t in range(1,11):
#     print(num*t)




# i=1
# while(i<=10):
#     print(i)
#     i+=1

num=879
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)