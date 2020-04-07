import random
import time

def gameplay():
    choiceforcomp = [82, 80, 83]
    computerchoice = random.choice(choiceforcomp)
    return computerchoice

index = 0
comp = 0
me = 0
R = 82
P = 80
S = 83
print('------WELCOME------')
name = input('\nEnter your name: ')
maxsc = input('\nEnter the maximum score for which the game is to be played: ')
check = maxsc.isdigit()
while check == False:
    maxsc = input('Please enter a valid digit: ')
    check = maxsc.isdigit()

choice = input('\n(R)OCK \n(P)APER \n(S)CISSORS \nEnter your move: ')
choice = choice.upper()

while(choice != 'R' and choice!='P' and choice!='S'):
    choice = input('Please enter the correct letter - R-Rock, P-Paper, S-Scissors - Enter now : ')
    choice = choice.upper()
while choice != 0 and index < int(maxsc):
     computerchoice = gameplay()
     if computerchoice == 82:
         computerchoice1 = 'R'
         print('\nOpponent has played Rock')
     elif computerchoice == 80:
         computerchoice1 = 'P'
         print('\nOpponent has played Paper')
     else:
         computerchoice1 = 'S'
         print('\nOpponent has played Scissors')

     if choice == computerchoice1:
         print('\nYou both have played the same move. So no points awarded')
     elif choice == 'R':
         if R > computerchoice:
             #print("\nOpponent has played: ", computerchoice1)
             print('Opponent has scored')
             comp = comp + 1
         else:
             print("\nYou have played: ", choice)
             print('You have scored')
             me = me + 1
     elif choice == 'P':
         if computerchoice == 82:
             print("\nYou have played: ", choice)
             print('You have scored')
             me = me + 1
         elif P < computerchoice:
             #print("\nOpponent has played: ", computerchoice1)
             print('Opponent has scored')
             comp = comp + 1
         else:
             print("\nYou have played: ", choice)
             print('You have scored')
             me = me + 1
     elif choice == 'S':
         if computerchoice == 82:
             #print("\nOpponent has played: ", computerchoice1)
             print('Opponent has scored')
             comp = comp + 1
         elif S > computerchoice:
             print("\nYou have played: ", choice)
             print('You have scored')
             me = me + 1
         else:
             #print("\nOpponent has played: ", computerchoice1)
             print('Opponent has scored')
             comp = comp + 1

     if index < int(maxsc)-1:
        choice = input('\n(R)OCK \n(P)APER \n(S)CISSORS \nEnter your move: ')
        choice = choice.upper()

        while (choice != 'R' and choice != 'P' and choice != 'S'):
             choice = input('Please enter the correct letter - R-Rock, P-Paper, S-Scissors - Enter now : ')
             choice = choice.upper()
     else:
         break
     index = index + 1

if comp == me:
    print('\nYou both are tied')
elif comp > me:
    print('\nComputer has won the game with a score of ', comp)
else:
    print('\nCongrats', str(name), '. You have won the game with a score of ', me)

print('\nSee ya next time pal!!!')
time.sleep(5)


