# rock = 1  1 1 
# paper = 2 2 2
# qainchi =3 3 3
import random
attempt=int(input("kitny attept?"))

win=0
lose=0
draw=0
while True:
    attempt-=1
    R=random.randint(1,3)
    User=int(input("select 1 for rock , 2 for paper , 3 for qainchi"))
    if R==User:
        draw+=1
        print("Draw",R,User)
    elif (R==1 and User==2) or (R==2 and User==3) or (R==3 and User==1) :
        win+=1
        print(" u win",R,User)
    else:
        lose+=1
        print("u lose",R,User)
    if attempt==0:
        print(f"wins:{win},loses:{lose},draws:{draw},game over")
        break