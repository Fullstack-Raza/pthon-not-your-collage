# info ={"naam":"Raza","Email":"email","age":20}
# info1 ={"naame":"taqy","Emaili":"emailo","agea":30}

# for i in info1:
#     info[i]=info1[i]

# print(info) 

# numbers={"a":10,"b":20,"c":30}
# sum=0
# for i in numbers:
#     sum+=(numbers[i])
# print(sum)

# l=["a","a","a","a","a","a","a","b","b","b","b","b","b","b"]

# d={}
# for i in l:
#     if i in d.keys():     
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

a={"a":10,"b":30,"c":40}
b={"c":40,"d":70}
for i in b:
    if i in  a.keys():
        a[i]+=b[i]
    else:
        a[i]=b[i]
print(a)