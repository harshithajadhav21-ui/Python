def amstrong():
    n=int(input("enter a number:-"))
    rev=0
    temp=n
    while(n>0):
        rem=n%10
        rev=rev+rem**3
        n=n//10
    if(temp==rev):
        print("number is amstrong number")
    else:
        print("number is not a amstrong number")
