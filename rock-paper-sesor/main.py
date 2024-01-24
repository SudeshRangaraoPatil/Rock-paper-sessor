import random

l = ["rock", "scissor", "paper"]
while True:
    ccount=0
    ucount=0
    uc = int(input('''
    game start....
    1 yes
    2 no | exit

    '''))
    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
            1 rock
            2 paper 
            3 sessor
            '''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            cchoice = random.choice(l)
            if cchoice==uchoice:
                print("compute value",cchoice)
                print("user choice",uchoice)
                print("game draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and cchoice=="scissor") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissor" and cchoice=="paper"):
                print("compute value", cchoice)
                print("user choice", uchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("compute value", cchoice)
                print("user choice", uchoice)
                print("computer win")
                ccount=ccount+1
        if ucount==ccount:
            print("final game draw...")
            print("user score",ucount)
            print("computer score",ccount)
        elif ucount>ccount:
            print("final you win the game...")
            print("user score", ucount)
            print("computer score", ccount)
        else:
            print("computer win the game better luck next time")
            print("user score", ucount)
            print("computer score", ccount)


    else:
        break