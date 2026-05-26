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
