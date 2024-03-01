import random

print("ROCK PAPER SCISSOR ")
print("___________________________________________________________________")
print("RULES :\n")
print("* Rock vs Paper --> Paper wins \n"
      "* Rock vs Scissors --> Rock wins \n"
      "* Paper vs Scissors --> Scissor wins \n")
print("____________________________________________________________________")
print("**********************GAME BEGINS*********************************")
while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice = int(input("Enter your choice :"))
    while choice > 3 or choice < 1:
        choice = int(input(''))

    if choice == 1:
        ch = 'Rock'
    elif choice == 2:
        ch = 'Paper'
    else:
        ch = 'Scissors'

    print('User choice = ', ch)
    print('Computers Turn....')

    ch1 = random.randint(1, 3)

    while ch1 == choice:
        ch1 = random.randint(1, 3)

    if ch1 == 1:
        c_choice = 'Rock'
    elif ch1 == 2:
        c_choice = 'Paper'
    else:
        c_choice = 'ScissoR'
    print("Computer choice is [*", c_choice, "*]")
    print(ch, 'Vs', c_choice)

    if choice == ch1:
        print('Its a Draw\n',)
        result = "DRAW"

    if (choice == 1 and ch1 == 2):
        print('-->paper wins\n')
        result = 'papeR'
    elif (choice == 2 and ch1 == 1):
        print('-->paper wins\n' )
        result = 'Paper'

    if (choice == 1 and ch1 == 3):
        print('-->Rock wins \n')
        result = 'Rock'
    elif (choice == 3 and ch1 == 1):
        print('-->Rock wins\n')
        result = 'rocK'

    if (choice == 2 and ch1 == 3):
        print('-->Scissors wins\n')
        result = 'scissoR'
    elif (choice == 3 and ch1 == 2):
        print('-->Scissors wins\n')
        result = 'Rock'

    if result == 'DRAW':
        print("*************** TIE ******************")
    if result == ch:
        print("************* USER WINS ******************")
        print("************* COMPUTER LOSES ******************")
        print("good play!,keep it up")
    else:
        print("*************COMPUTER WINS****************")
        print("************* USER LOSES ******************")
        print("well played,try again")
    print("Do you want to play again? (Y/N)")
    ans = raw_input()
    if ans == 'N':
        break

print("thank you for playing")
print("____________________________________________________________________")