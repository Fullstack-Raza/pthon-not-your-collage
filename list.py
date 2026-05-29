# Numbers=[3,-1,4,-5,9]
# positive=[]
# nagitive=[]
# for i in Numbers:
#     if i>=0:
#         positive.append(i)
#     else:
#         nagitive.append(i)
# print(f"p+ numbers = {positive},  n- numbers={nagitive}")







# Numbers=[3,-1,4,-5,9]
# pos=[]
# neg=[]

# for i in Numbers:
#     if i>=0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(f"positive numbers are:{pos}, negetive numbers are: {neg}")

# numbers=[10,20,30,40]
# mean=0
# for i in numbers:
#     mean+= i
# mean /= len(numbers)
# print(f"the avrage of ur numbers is: {mean}")

# l=[4,8,2,9,1]
# per=l[0]
# biggestnumindex=0
# for i in range(len(l)):
#     if l[i]>per:
#         biggestnumindex=i
#         per=l[i]

# print(f"biggest number is:{per} and its index: {biggestnumindex}")

# l=[4,8,2,9,1] 
# biggest=l[0]
# big=l[0]

# for i in l:
#     if i> biggest:
#         big=biggest
#         biggest=i
       
      

# print(f"secound big : {big}")
# print(f"biggest : {biggest}")

# l=[4,8,2,9,1] 
# big=l[0]
# secBig=l[0]

# for i in l:
#     if i>big:
#         secBig=big
#         big=i
#     elif i>secBig:
#         secBig=i
# print(f"the sec big number is {secBig}")
l=[1,3,5,7]

for i in range(len(l)-1):
    if l[i]> l[i+1]:
        print("list is not sorted")
        break
else:
    print("list is sorted")

