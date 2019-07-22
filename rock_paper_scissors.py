import random
import time

player_score = 0
computer_score = 0
player_moves = {'rock' : 0, 'paper' : 0, 'scissors' : 0}

def promptPlay():
    response = input('Do you want to play y/n ? or sc for scoreboard ').lower()
    if(response == 'y'):
        playGame()
    elif(response == 'n'):
        print('Thank you for playing!')
    elif(response == 'sc'):
        showScores()

def showScores():
    global player_score
    global computer_score
    print('You won ' + str(player_score) + '/' + str((player_score + computer_score)) + ' games vs comp!')
    promptPlay()

def whatMove(i):
    if i == 0:
        return 'rock'
    elif i == 1:
        return 'paper'
    elif i == 2:
        return 'scissors'

def computerMove():
    global player_moves
    # computer does not have access to immediate player move
    # computer has access to past data of the player
    sensitivity = 3  # inversely proportinal to sensitivity
    response_treshold = 3
    # below conditionals reduce computer predictability
    if player_moves['rock'] > response_treshold:
        player_moves['rock'] -= 2
        player_moves['paper'] -= 1
        player_moves['scissors'] -= 1
    if player_moves['paper'] > response_treshold:
        player_moves['rock'] -= 1
        player_moves['paper'] -= 2
        player_moves['scissors'] -= 1
    if player_moves['scissors'] > response_treshold:
        player_moves['rock'] -= 1
        player_moves['paper'] -= 1
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

def playGame():
    global player_moves
    global player_score
    global computer_score

    ai_move = computerMove()
    
    choice = input('Make a move! r (rock) p (paper) s(scissors)  sc(scoreboard) ').lower()
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
        showScores()

    result = move - ai_move

    if result == 0:
        print('Draw! > Computer made the same move')
        promptPlay()
    elif result == 1 or result == -2:
        print('You chose ' + whatMove(move) + ' and the computer chose ' + whatMove(ai_move) + '. You Win!')
        player_score += 1
        promptPlay()
    elif result == 2 or result == -1:
        print('You chose ' + whatMove(move) + ' and the computer chose ' + whatMove(ai_move) + '. You Lost!')
        computer_score += 1
        promptPlay()
    
print('######## Rock Paper Scissors Game #########')
promptPlay()