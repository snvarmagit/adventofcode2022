import os

elf_group = []

class Elf:

    def __init__(self, input) -> None:
        self.cal_list = input

    def __repr__(self):
        return "(" + repr(self.cal_list) + "," + str(self.getcalsum()) + ")"

    def getcalsum(self):
        return sum(self.cal_list)

def load_input(file):
    ''' Load input '''
    global elf_group
    elf_group = []

    file_abspath =  os.path.join(os.path.dirname(__file__), file)
    tmp = []
    with open(file_abspath) as f:
        for line in f:
            x = line.strip()
            if len(x):
                tmp.append(int(x))
            else:
                elf_group.append(Elf(tmp.copy()))
                tmp.clear()
        elf_group.append(Elf(tmp.copy()))

def do_part1(file):
    ''' Part1 Solution '''
    load_input(file)
    sorted_list = sorted(elf_group, key= lambda p: p.getcalsum(), reverse=True)

    return sorted_list[0].getcalsum()

def do_part2(file):
    ''' Part2 Solution '''
    load_input(file)
    sorted_list = sorted(elf_group, key= lambda p: p.getcalsum(), reverse=True)

    return sorted_list[0].getcalsum() + sorted_list[1].getcalsum() + sorted_list[2].getcalsum()

if __name__ == '__main__':
 
    print( 'Part 1: ', do_part1('input.txt'))
    print( 'Part 2: ', do_part2('input.txt'))

