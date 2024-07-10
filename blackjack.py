logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def choice():
    if(S>R):
        print("User won")
    elif(S<R):
        print("Computer won")
    else:
        print("Draw")
print(logo)
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
a=random.sample(cards,2)
b=random.sample(cards,2)
print("Your cards are:",a)
print("One of the computer card is:",b[0])
sum=0
S=0
R=0
su=0
A=len(a)
for i in range(0,A):
    sum+=a[i]
print("Your current score is",sum)
Sum=0
B=len(b)
for j in range(0,B):
    Sum+=b[j]
win1=1
win2=1
if(sum==21):
    win1=0
elif(Sum==21):
    win2=0
if(win2 or win1==0):
    if(win1 and win2==0):
        print("Draw")
        hi=False
    elif(win1==0):
        print("User won")
        hi=False
    elif(win2==0):
        print("Computer won")
        hi=False
if(sum == 0):
    print("User won")
elif(sum > 21):
    print("Computer won")
else:
    hi=True
    while hi==True:
        newcard=input("Type 'y' to get another card, type 'n' to pass:")
        if (newcard=="y"):
            S=0
            card=random.choice(cards)
            a.append(card)
            print(a)
            W=len(a)
            for i in range(0,W):
                S+=a[i]
            print("Your current score is",S)
            if(S>21):
                print("Computer won")
                hi=False
            elif(S==21):
                print("User won")
                hi=False
            else:
                hi=True
            
        elif (newcard=="n"):
            while(Sum<17):
                card=random.choice(cards)
                b.append(card)
                Sum=0
                for i in range(0,len(b)):
                    Sum+=b[i]
                if(Sum>21):
                    print("User won")
                    hi=False
                elif(Sum == 21):
                    print("Computer won")
                    hi=False
            if(Sum>17 and Sum<21):
                for i in range(0,len(a)):
                    su+=a[i]
                if(su<Sum):
                    print("Computer won")
                    break
                elif(su>Sum):
                    print("User won")
                    break
                else:
                    print("Draw")
                    break
if(R==0):
    R=b[0]+b[1]
print("The computer cards are",b)
print("Computer score is:",Sum)
                            
            
                                

