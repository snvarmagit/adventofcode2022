import os

section_pairs_list = []

def load_input(file):
    ''' Define input datastructure '''
    global section_pairs_list
    section_pairs_list = []

    file_abspath =  os.path.join(os.path.dirname(__file__), file)
    with open(file_abspath) as f:
        for line in f:
            pair = [tuple([ int(_) for _ in section.split('-')]) for section in line.strip().split(',')]
            section_pairs_list.append(pair)

def do_part1(file):
    ''' Part1 Solution '''
    load_input(file)
    count = 0
    for pair in section_pairs_list:
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        if x1 >= x2 and y1 <= y2:
            count = count + 1
        elif x2 >= x1 and y2 <= y1:
            count = count + 1
    return count

def do_part2(file):
    ''' Part2 Solution '''
    load_input(file)
    count = 0
    for pair in section_pairs_list:
        x1, y1 = pair[0]
        x2, y2 = pair[1]

        if x1 in range(x2, y2+1) or y1 in range(x2, y2+1):
            count = count + 1
        elif x2 in range(x1, y1+1) or y2 in range(x1, y1+1):
            count = count + 1
    return count

if __name__ == '__main__':
    print( 'Part 1 Sol: ', do_part1('input.txt'))
    print( 'Part 2 Sol: ', do_part2('input.txt'))