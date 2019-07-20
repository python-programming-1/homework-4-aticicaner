import random
import time


def promptPlay():
    response = input('Do you want to play y/n ?').lower()
    if(response == 'y'):
        playGame(0,0) #init game with 0 score
    elif(response == 'n'):
        print('Thank you for playing!')

# ps > player_score
# cs > computer_score

def playGame(ps,cs):
    choice = input('Make a move! r (rock) p (paper) s(scissors)  sc(scoreboard) ').lower()
    if choice == 'r':
        move = 0
    elif choice == 'p':
        move = 1
    elif choice == 's':
        move = 2
    elif choice == 'sc':
        showScores(ps,cs)
    else:
        print('Please enter a valid move')
        playGame(ps,cs)

    random.seed(time.time())
    ai_move = random.randint(0,2)

    result = move - ai_move

    if result == 0:
        print('Draw! > Computer made the same move')
        playAgain(ps,cs)
    elif result == 1 or result == -2:
        print('You won! > Computer made ' + whatMove(ai_move) + ' versus your ' + whatMove(move))
        ps += 1
        playAgain(ps,cs)
    elif result == 2 or result == -1:
        print('You lost! > Computer made ' + whatMove(ai_move)+ ' versus your ' + whatMove(move))
        cs += 1
        playAgain(ps,cs)


def showScores(ps,cs):
    print('You won ' + str(ps) + '/' + str((ps + cs)) + ' games')
    playAgain(ps,cs)


def playAgain(ps,cs):
    choice = input('Do you want to play again? y/n or sc for scoreboard').lower()
    if choice == 'y':
        playGame(ps,cs)
    elif choice == 'n':
        print('Thank you for playing!')
    elif choice == 'sc':
        showScores(ps,cs)

def whatMove(i):
    if (i == 0):
        return 'rock'
    elif i == 1:
        return 'paper'
    elif i == 2:
        return 'scissors'
    

print('######## Rock Paper Scissors Game #########')
promptPlay()