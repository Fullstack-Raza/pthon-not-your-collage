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

# nf=int(input("give a nmbr for factors:-"))
# sumOfF=0
# for i in range(1,nf,):
#     if nf%i==0:
#         sumOfF+=i

# if sumOfF==nf:
#      print("its a perfect num")  
# else:
#     print("its not a perfect num")

# nf=int(input("give a nmbr for factors:-"))
# isPrime=0
# for i in range(1,nf+1,1):
#     if nf%i==0:
#         isPrime = isPrime+1
# if isPrime==2:
#     print("ea num prime hy ")
# else:
#     print("not prime")







# nP=int(input("tell me a number: - "))
# saving=0
# for i in range(1,nP+1,1):
#     if nP%i==0:
#         saving= saving+1
# if saving==2:
#     print("its prime")
# else:
#     print("its composite")

# word= "raza"
# revWord=""
# for i in range(-1,(-len(word))-1,-1):
#     revWord+=word[i]
# print(revWord)



# word=input("give us a word to reverse")
# saving=""
# for i in range(-1,-len(word)-1,-1):
#     saving+=word[i]

# if word==saving:
#     print("its palindrome")
# else:
#      print("its not palindrome")


# word="Raza333##"
# isalpha=0
# isdigite=0
# scahr=0
# for i in word:
#    if i.isalpha():
#       isalpha+=1
#    elif i.isdigit():
#       isdigite+=1
#    else:
#       scahr+=1
# print(isalpha,isdigite,scahr)
      

#    /////// while loop 
# a=int(input("give me a number:- "))
# while a>0:
#     print(a%10)
#     a= a//10


# a=int(input("give me a number:- "))
# rev=0
# while a>0:
#     rev= (rev*10)+(a%10)
#     a//=10
# print(rev)







# nmbr=int(input("give us a nmbr to reverse:-"))
# realNmbr=nmbr
# rev=0
# while realNmbr>0:
#     rev= rev*10 + realNmbr%10
#     realNmbr//=10
# print(nmbr)
# print(rev)
# if nmbr==rev:
#     print("its palindrome")
# else :
#     print("its NoT palindrome")






import random
randomNum= random.randint(1,100)
UserNum=int(input("guess kron 0 sy 100 tk :- "))
tryes=0
if randomNum==UserNum:
    tryes+=1
    print(f"good game ap ny game ko khatam kra {tryes} gusses me ")
else:
    while randomNum!=UserNum:
        tryes+=1
        if UserNum<randomNum:
            print("apka num low hy asl number sy ")
            UserNum=int(input("guess kron 100 sy 0 tk :- "))
        elif UserNum>randomNum:
            print("apka num high hy asl num st ")
            UserNum=int(input("guess kron 100 sy 0 tk :- "))
    else :
         tryes+=1
         print(f"good game ap ny game ko khatam kra {tryes} gusses me ")

    

