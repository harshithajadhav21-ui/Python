# FILE HANDLING
# read -- open the file for reading
# write -- open the file for writing but it erases/vanishes the older data and adds the new data
# append -- open the file and adds the new data below the older one , creates a file not exist
# create -- creates a file and adds the info in it , gives error if the file exist

# f=open("demo.txt",'w')
# f.write("hello, good morning")
# f.close()

# f=open("demo.txt",'r')
# print("file_name",f.name)
# print("readble_mode",f.readable())
# print("writable_mode",f.writable())
# print("file_close",f.closed)
# # f.close()

# print(f.read())
# f.close()

# WRITE DATA USING WRITE  BUT EXISTING DATA IS ALREADY REMOVED
# f=open("demo.txt",'w')
# f.write("hello I'm harshitha \n")
# f.close()

# WRITE DATA USING APPEND BUT THE DATA REMAINS SAME AND NEW DATA IS ADDED TO THE EXISTING FILE
# f=open("demo.txt",'w')
# f.write("hello I'm harshitha \n")
# f.write("im from sangli")
# f.close()

# READ LINES
# single line
# f=open("demo.txt",'r')
# print(f.readline())

# two lines
# f=open("demo.txt",'r')
# print(f.readlines())
# print(f.readline())

# f=open("demo.txt","r")
# for x in f:
#     print(x)

# f=open("demo.txt","x")
f1=open("demo1.txt",'w')
f1.write("good morning")
f1.read("demo1.txt","r")
print(f1.readline())
f1.close()