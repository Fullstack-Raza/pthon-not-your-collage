# file=open("R.txt",'w')
# data=input("kia likhna hy bhauiiaaa jiiiiiii")
# file.write(data)
# file = open("R.txt",'r')
# print(file.read())


# file=open("file.txt", 'r')
# # data=input("tell me something that will be added in my file.")
# # file.write(data)

# print(file.read())
# with open("file.txt",'r')as f:
#     print (f.read())


def createfile():
    print("your file created")
def readfile():
    print("your file is ready to be readed")
def updatefile():
    print("now you can update your file")
def deletefile():
    print("your file deleted")


print("for creating file please press 1")
print("for reading file please press 2")
print("for updating file please press 3")
print("for deleting file please press 4")

nmbr=int(input("what you want to do:-"))

if nmbr==1:
    createfile()
if nmbr==2:
    readfile()
    
if nmbr==3:
    updatefile()
if nmbr==4:
    deletefile()

