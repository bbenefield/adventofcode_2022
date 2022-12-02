with open('day2/day2_input.txt', 'r') as fin:
    cheat_codes = fin.readlines()

# A = Rock
# B = Paper
# C = Scissors

# X = Lose
# Y = Draw
# Z = Win

elf_to_me_translation = {'A': 'X', 'B': 'Y', 'C': 'Z'}
hand_shape = {'X': 1, 'Y': 2, 'Z': 3}
round_score = {'Win': 6, 'Lose': 0, 'Draw': 3}
strategy = {
    'X': {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }, 
    'Y': {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'        
    }, 
    'Z': {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'    
    }
}

total_score = 0

for round in cheat_codes:       
    game_pair = round.strip().split(' ')
    
    game_pair[1] = strategy[game_pair[1]][game_pair[0]]
    
    if elf_to_me_translation[game_pair[0]] == game_pair[1]:
        total_score += (round_score['Draw'] + hand_shape[game_pair[1]])
    elif game_pair[0] == 'A' and game_pair[1] == 'Y':
        total_score += (round_score['Win'] + hand_shape[game_pair[1]])
    elif game_pair[0] == 'B' and game_pair[1] == 'Z':
        total_score += (round_score['Win'] + hand_shape[game_pair[1]])
    elif game_pair[0] == 'C' and game_pair[1] == 'X':
        total_score += (round_score['Win'] + hand_shape[game_pair[1]])
    else:
        total_score += hand_shape[game_pair[1]]
        
    print(f'Round Score: {total_score}')
        
print(f'Score: {total_score}')