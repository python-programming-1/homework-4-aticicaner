import random
import time

def whatMove(i):
    if (i == 0):
        return 'rock'
    elif i == 1:
        return 'paper'
    elif i == 2:
        return 'scissors'

def computerMove():
    random.seed(time.time())
    return random.randint(0,2)

again = False
initial_input = False

player_score = 0
computer_score = 0
game_on = True
player_moves = {'rock' : 0, 'paper' : 0, 'scissors' : 0}


print('######## Rock Paper Scissors Game #########')
while game_on == True:
    while initial_input == False:
        if again == False:
            response = input('Do you want to play y/n ?(sc for scoreboard)  ').lower()
        elif again == True:
            response = input('Do you want to play again y/n ?(sc for scoreboard)  ').lower()
        
        if(response == 'y'):
            initial_input = True
        elif(response == 'n'):
            print('Thank you for playing!')
            initial_input = True
            game_on = False
            break
        elif response == 'sc':
            print('You won ' + str(player_score) + '/' + str((player_score + computer_score)) + ' games')
            again = True
            initial_input = False
            continue
        else:
            print('Please use a valid input')
    if game_on == True:
        choice = input('Make a move! r (rock) p (paper) s(scissors)  sc(scoreboard)  ').lower()
        if choice == 'r':
            move = 0
            player_moves['rock'] += 1
        elif choice == 'p':
            move = 1
            player_moves['paper'] += 1
        elif choice == 's':
            move = 2
            player_moves['scissors'] += 1
        elif choice == 'sc':
            print('You won ' + str(player_score) + '/' + str((player_score + computer_score)) + ' games')
            again = True
            initial_input = False
            continue
        else:
            print('Please use a valid input')
            continue

        computer_move = computerMove()
        result = move - computer_move
        if result == 0:
            print('Draw! > Computer made the same move')
        elif result == 1 or result == -2:
            print('You chose ' + whatMove(move) + ' and the computer chose ' + whatMove(computer_move) + '. You Win!')
            player_score += 1
        elif result == 2 or result == -1:
            print('You chose ' + whatMove(move) + ' and the computer chose ' + whatMove(computer_move) + '. You Lose!')
            computer_score += 1

        again = True
        initial_input = False
