import random
import time

def whatMove(i):
    if (i == 0):
        return 'rock'
    elif i == 1:
        return 'paper'
    elif i == 2:
        return 'scissors'
# 0 > rock  1 > paper  2 > scissors

def computerMove():
    # computer does not have access to immediate player move
    # computer has access to past data of the player
    sensitivity = 3  # inversely proportinal to sensitivity
    response_treshold = 5
    # below conditionals reduce computer predictability
    if player_moves['rock'] > response_treshold:
        player_moves['rock'] -= 2
        player_moves['paper'] -= 3
        player_moves['scissors'] -= 3
    if player_moves['paper'] > response_treshold:
        player_moves['rock'] -= 3
        player_moves['paper'] -= 2
        player_moves['scissors'] -= 3
    if player_moves['scissors'] > response_treshold:
        player_moves['rock'] -= 3
        player_moves['paper'] -= 3
        player_moves['scissors'] -= 2
    # below parameters are for computers ability to predict player patterns
    random.seed(time.time())
    rock = random.randint(0,sensitivity) + player_moves['scissors']
    random.seed(time.time())
    paper = random.randint(0,sensitivity) + player_moves['rock']
    random.seed(time.time())
    scissors = random.randint(0,sensitivity) + player_moves['paper']
    move_pool = [rock, paper, scissors]
    return move_pool.index(max(move_pool))

# menu and game flow parameters
# these booleans determine where in the loop user lands after selecting an option
again = False
initial_input = False

player_score = 0
computer_score = 0
game_on = True
player_moves = {'rock' : 0, 'paper' : 0, 'scissors' : 0}

# conditional statements below are not for decisions of the computer
# they govern the menu and game flow
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
    if game_on == True:  # below play input is taken and recorded in player_moves dict
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
        # computer move asked here, it has no access to current move
        computer_move = computerMove()
        result = move - computer_move
        # determining the round output mathematically
        if result == 0:
            print('Draw! > Computer made the same move')
        elif result == 1 or result == -2:
            print('You chose ' + whatMove(move) + ' and the computer chose ' + whatMove(computer_move) + '. You Win!')
            player_score += 1
        elif result == 2 or result == -1:
            print('You chose ' + whatMove(move) + ' and the computer chose ' + whatMove(computer_move) + '. You Lose!')
            computer_score += 1
        # ask if they want to play again and move up to the top of the loop
        again = True
        initial_input = False
