import random
import sys

# Step 1: Starting information
print('Welcome to RPS')
moves: dict = {'rock':'R', 'paper':'P', 'scissors':'S'}
valid_moves: list = list(moves.keys())

#Step 2 Scoring Variables
ai_score: int = 0
user_score: int = 0

#Step 3 :The Infinite Loop
while True:
    user_move: str = input('Rock, Paper or Scissors?>>  ').lower()
    ai_move: str = random.choice(valid_moves).lower()
    if user_move=='exit':
        print('Thanks for playing!')
        print(f'You: {user_score}')
        print(f'AI: {ai_score}')

        sys.exit()
    elif user_move not in valid_moves:
        print('Invalid move..')
        continue
    elif user_move == ai_move:
        print('It\'s a tie!')

    elif user_move == 'rock' and ai_move == 'scissors':
        user_score += 1
        print('You win!')

    elif user_move == 'paper' and ai_move == 'rock':
        print('You win!')
        user_score += 1

    elif user_move == 'scissors' and ai_move == 'paper':
        print('You win!')
        user_score += 1

    else:
        print('You lose..')
        ai_score += 1

    print('------')
    print(f'You: {moves[user_move]}')
    print(f'AI: {moves[ai_move]}')
    print('------')