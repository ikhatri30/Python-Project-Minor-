import random
x= ("Snake", "Water", "Gun")
print("Choose from the following options:")
print("Snake, Water, Gun")
play= True

while play:
    p= None
    c= random.choice(x)
    while p not in x:
        p= input("Enter a choice: ")
    else:
        print("Player 1:",p)
        print("Computer's choice:",c)
    if(p==c):
        print("MATCH TIED")
    elif(p=="Snake" and c=="Water"):
        print("YOU WON")
    elif(p=="Water" and c=="Gun"):
        print("YOU WON")
    elif(p=="Gun" and c=="Snake"):
        print("YOU WON")
    else:
        print("YOU LOSE")

    ch= input("PLAY AGAIN? (y/n)")
    if not (ch=="y"):
        play= False

print("THANKS FOR PLAYING!")

    
