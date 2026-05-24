# num=int(input("num:- "))
# for i in range(10+1): 
#     print(num*i)



# count= int(input("give me a nmbr:- "))
# for things in range (100,200):
#     print(count*things)


# name= "taqi"
# for i in range(len(name)):
#     print(name[i])


# a="raza"
# print(len(a))

# for i in range(1,11,1):
#     if i<=3 or i>8:
#         continue
#     print(i)    

# for i in range(1,11,1):
#     if i>=3 and i<8:
#         continue
#     print(i) 






# word="hello world"
# range3= int(input("how many time should i print: - "))
# for i in range (1,range3+1,1):
#     print (i)


# nmbr=int(input("tell me a nmr please"))
# for i in range(nmbr,0,-1):
#     print (i)

# numOfTable=int(input("konsy num ka table chaea:- "))
# for i in range(1,11,1):
#     print(f"{numOfTable}x{i}={numOfTable*i}")

# 5
# 1+2+3+4+5

# numOfSum=int(input("konsy num ka sum chaea:- "))
# soom = 0 
# for i in range(1,numOfSum+1,1):
#     soom+=i

# print(soom)
    






# numForSum=int(input("give me a number to make sum:- "))
# soom=0
# for i in range(1,numForSum+1,1):
#     soom+=i

# print(soom)

# 5
# 1*2*3*4*5
    
# n=int(input("give nmbr for factorial:_"))
# f=1
# for i in range(1,n+1,1):
#     f*=i

# print(f)







# n = 10
# o 1,3,5,7,9,
# e 2,4,6,8,10
# n=int(input("tell me a nmbr for geting the e:-"))
# n=int(n/2)
# if n%2==0:
#     print(n)
# else:
#     print(n+1)
# n=int(input("give num :- "))
# o=0
# e=0
# for i in  range(1,n+1,1):
#     if i%2==0:
#         e+=i
#     elif i%2==1:
#         o+=i
# print(e,o)







# n=int(input("give a random nmbr:-"))
# so=0
# se=0
# for i in range(1,n+1):
#     if i%2==0:
#         so+=i
#     elif i%2==1:
#         se+=i
# print(so,se)

# n=int(input("give a random nmbr for fevtors:-"))

# for i in range(1,n+1,1):
#     if n%i==0:
#         print(i)

nf=int(input("give a nmbr for factors:-"))
sumOfF=0
for i in range(1,nf,):
    if nf%i==0:
        sumOfF+=i
print(sumOfF)