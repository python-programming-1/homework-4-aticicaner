## Solution explanation
Methods are governing the overall structure of the game

Parameters are used globally to aviod bouncing variables around

Computer has no access to immediate user input
The computer difficulty is purely subjectively advantageous against certain playstyle as it has 50 % chance to win/lose against random inputs. If you falsely seek the pattern the computer punishes you, the objective is to get the 1 step ahead of the player which is speculative in nature as 2 steps forward is 1 step back in rock paper scissors, and it layers modularly. 



# Homework 4

# Let's Make A Game! 
## Can you make rock paper scissors?

For this assignment you'll make a rock paper scissors game!

1. git clone this repository like you did in homework 2 and 3
2. create a file named rock_paper_scissors.py inside your repository (repo) folder on your machine.
3. When you run your program, it should prompt the user by printing "make a move! (r/s/p):"
4. Your program should accept 6 inputs from a user: 'r' for rock, 'p' for paper, 's' for scissors and 'y' for yes and 'n' for no, 'sc' for score.
5. Your program should randomly select a move. See https://docs.python.org/3/library/random.html for reference.
5. Your program should output the following line with one of the options (rock, paper, scissors) for the computer and yourself:
'You chose rock/paper/scissors and the computer chose rock/paper/scissors. You Win/Lose!
6. After a game, the computer should ask you 'Do you want to play again? (y/n)?' If you enter 'y' the game should start over, if you enter 'n' the program should exit after saying "thanks bye!".
7. If a player inputs 'sc' return a score like: 'human: X, computer: Y' where X and Y are the respective scores.
8. Bonus: Can you make the computer smarter? Instead of a random move, have the computer make a move based on the player's history of moves.
So if the player has played scissor three times, the computer may try to play rock.

Sample output:

    >>Make a move! (r/s/p)
    r
    >> You chose rock and the computer chose scissors. You win!
    sc
    >> human: 1, computer: 0
    >> Do you want to play again? (y/n)
    n
    >>Thanks bye!

9. Follow the instructions as precisely as possible, but feel free to ask me for clarification. You'll want to use loops like a while loop to repeat certain instructions, like asking a user to play again, and if/else statements to help your program handle the different possible outcomes that your game of rock paper scissors may generate. You may use a list or some other data structure to store the history of player moves for #8.
