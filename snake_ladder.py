import random

#Snake and ladder positions
snake_ladder_positions = {
    1: 38, 4:14, 9: 31, 17:6, 21:42,
    28: 84, 51: 57, 54: 34, 62: 9, 64: 60,
    72: 91, 80: 99, 87:36, 93: 73, 95: 75, 98: 79}

#Dice roll function
def dice_roll():
    return random.randint(1, 6)

#Function to get player posistion after dice roll
def get_position(current_position, player_name):
    result = dice_roll()
    print(f'{player_name} rolled a {result}')
    new_position = min(current_position + result, 100) # Limit position to 100

    if new_position in snake_ladder_positions:
        new_position = snake_ladder_positions[new_position]
        if new_position > current_position:
            print(f'You climbed a ladder to a position: {new_position}')
        else:
            print(f'Oops! You got bitten by a snake and moved down to position: {new_position}')
    return new_position

#Play function
def play(player1_name, player2_name):
    player1_position = 0
    player2_position = 0
    winner = None

    print('Welcome to Snake and Ladder Game!')
    print('Rules:')
    print('1.Roll the dice to move forward.')
    print('2.Climb up the ladder if you land at the bottom.')
    print('3.Slide down the snake if you land at the head.')
    print('4.The first player to reach position 100 wins.')

    while True:
        input(f'{player1_name}, press Enter to roll the dice')
        player1_position = get_position(player1_position, player1_name)
        print(f'{player1_name}`s current position: {player1_position}')
        if player1_position == 100:
            winner = player1_name
            break

        input(f'{player2_name}, press Enter to roll the dice')
        player2_position = get_position(player2_position, player2_name)
        print(f'{player2_name}`s current position: {player2_position}')
        if player2_position == 100:
            winner = player2_name
            break

    print(f'Congratulations {winner}! You won the game!')

play('Joshua', 'Joy')