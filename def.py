n=18
print("gusse game")

for i in range(4):
    x=int(input("Gusse Your number in 1 to 50:"))
    if x<=50 and x>0:
        if x<n:
            print("your number is very low")
        elif x>n:
            print("your number is very high")
        else:
            break
    else:
        break
        print("game Over: You choose wronge number")
if x==n:
    print("You are Winner!!!")
else:
    print("Game Over")