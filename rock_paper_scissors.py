import random
import time

player_score = 0
computer_score = 0
player_moves = {'rock' : 0, 'paper' : 0, 'scissors' : 0}

# handling wrong inputs without crashing the game
# makes sure user returns to proper place back safely
def wrongInput(input_type):
    if input_type == 1:
        print('Please enter a valid input y/n/sc!')
        promptPlay()
    elif input_type == 2:
        print('Please enter a valid input r/p/s/sc!')
        playGame()

# user prompt to ask if they want to play
def promptPlay():
    response = input('Do you want to play y/n ? or sc for scoreboard ').lower()
    if(response == 'y'):
        playGame()
    elif(response == 'n'):
        print('Thank you for playing!')
        quit()
    elif(response == 'sc'):
        showScores()
    else:
        wrongInput(1)

# display scores and return to menu
def showScores():
    global player_score
    global computer_score
    print('You won ' + str(player_score) + '/' + str((player_score + computer_score)) + ' games vs comp!')
    promptPlay()

# query which move numerically to string
def whatMove(i):
    if i == 0:
        return 'rock'
    elif i == 1:
        return 'paper'
    elif i == 2:
        return 'scissors'

# mediocre and arguably terrible AI implementation to operate computer action
# but I did try and it did decent job countering me until I figured out how to beat it
def computerMove():
    global player_moves
    # computer does not have access to immediate player move
    # computer has access to past data of the player
    sensitivity = 3  # inversely proportinal to sensitivity: 0 for most sensitive
    response_treshold = 4
    reduction_rate = 2
    # below conditionals reduce computer predictability
    if player_moves['rock'] > response_treshold:
        player_moves['rock'] -= reduction_rate
    if player_moves['paper'] > response_treshold:
        player_moves['paper'] -= reduction_rate
    if player_moves['scissors'] > response_treshold:
        player_moves['scissors'] -= reduction_rate
    # below parameters are for computers ability to predict player patterns
    random.seed(time.time())
    rock = random.randint(0,sensitivity) + player_moves['scissors']
    random.seed(time.time())
    paper = random.randint(0,sensitivity) + player_moves['rock']
    random.seed(time.time())
    scissors = random.randint(0,sensitivity) + player_moves['paper']
    move_pool = [rock, paper, scissors]
    if rock == paper or rock == scissors or paper == scissors:
        random.seed(time.time())
        return random.randint(0,2)
    return move_pool.index(max(move_pool))

# game main 
# collects AI play first so it doesn't get influenced by player input
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
    else:
        wrongInput(2)

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

# main call to start the application
print('######## Rock Paper Scissors Game #########')
promptPlay()