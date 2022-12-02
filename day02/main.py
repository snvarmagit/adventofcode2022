import os

play_input = []
player1_map = dict([('A', 'Rock' ), ('B', 'Paper'), ('C', 'Scissors')])
player2_map = dict([('X', 'Rock' ), ('Y', 'Paper'), ('Z', 'Scissors')])
score_map = dict([('Rock', 1 ), ('Paper', 2), ('Scissors', 3)])

def load_input(file):
    global play_input
    play_input = []
    ''' Create Input Data structure '''
    file_abspath =  os.path.join(os.path.dirname(__file__), file)
    with open(file_abspath) as f:
        for line in f:
            play_input.append(tuple(line.strip().split(' ')))
    
def getscore_part1(x, y):
    score = 0
    if player1_map[x] == 'Rock':
        if player2_map[y] == 'Paper':
            score = score_map['Paper'] + 6
        elif player2_map[y] == 'Scissors':
            score = score_map['Scissors'] + 0
        else:
            score = score_map['Rock'] + 3
    elif player1_map[x] == 'Paper':
        if player2_map[y] == 'Rock':
            score = score_map['Rock'] + 0
        elif player2_map[y] == 'Scissors':
            score = score_map['Scissors'] + 6
        else:
            score = score_map['Paper'] + 3
    else:
        if player2_map[y] == 'Rock':
            score = score_map['Rock'] + 6
        elif player2_map[y] == 'Paper':
            score = score_map['Paper'] + 0
        else:
            score = score_map['Scissors'] + 3

    return score

def getscore_part2(x, result):
    score = 0
    if player1_map[x] == 'Rock':
        if result == 'win':
            score = score_map['Paper'] + 6
        elif result == 'lose':
            score = score_map['Scissors'] + 0
        else:
            score = score_map['Rock'] + 3
    elif player1_map[x] == 'Paper':
        if result == 'lose':
            score = score_map['Rock'] + 0
        elif result == 'win':
            score = score_map['Scissors'] + 6
        else:
            score = score_map['Paper'] + 3
    else:
        if result == 'win':
            score = score_map['Rock'] + 6
        elif result == 'lose':
            score = score_map['Paper'] + 0
        else:
            score = score_map['Scissors'] + 3

    return score

def do_part2(file):
    '''Part 1 Solution'''
    load_input(file)
    column_decode = dict([('X', 'lose'), ('Y', 'draw'), ('Z', 'win')])
    total_score = 0
    for round in play_input:
        x , y = round
        total_score = total_score + getscore_part2(x, column_decode[y])

    return total_score

def do_part1(file):
    '''Part 2 Solution'''
    load_input(file)
    total_score = 0
    for round in play_input:
        total_score = total_score + getscore_part1(*round)

    return total_score

if __name__ == '__main__':
    print('Part 1 Sol:', do_part1('input.txt'))
    print('Part 2 Sol:', do_part2('input.txt'))