import os
import string

rucksacks_list = []
priority_map = dict(zip(list(string.ascii_lowercase + string.ascii_uppercase), list(range(1,53))))

def load_input(file):
    ''' Define input datastructure '''
    global rucksacks_list
    rucksacks_list = []

    file_abspath =  os.path.join(os.path.dirname(__file__), file)
    with open(file_abspath) as f:
        for line in f:
            part_one = list(line[:(len(line)//2)])
            part_two = list(line[(len(line)//2):len(line)-1])
            rucksacks_list.append((part_one, part_two))

def do_part1(file):
    ''' Part1 Solution '''
    load_input(file)
    sum = 0
    for rucksack in rucksacks_list:
        part1, part2 = rucksack
        common_item = set(part1) & set(part2)
        item = common_item.pop()
        sum = sum + priority_map[item]
    return sum

def do_part2(file):
    ''' Part2 Solution '''
    load_input(file)
    sum = 0
    i = 0
    while i < len(rucksacks_list):
        set_one = set(rucksacks_list[i][0] + rucksacks_list[i][1])
        set_two = set(rucksacks_list[i+1][0] + rucksacks_list[i+1][1])
        set_three = set(rucksacks_list[i+2][0] + rucksacks_list[i+2][1])

        badge_type = set_one & set_two & set_three
        item = badge_type.pop()

        sum = sum + priority_map[item]
        i = i + 3
    return sum

if __name__ == '__main__':
    print( 'Part 1 Sol: ', do_part1('input.txt'))
    print( 'Part 2 Sol: ', do_part2('input.txt'))