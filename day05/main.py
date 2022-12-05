import os

crates_stack_map = {}
procedure_steps = []

def load_input(file):
    ''' Define Input datastructure '''
    global crates_stack_map
    global procedure_steps

    crates_stack_map = {}
    procedure_steps = []

    file_abspath =  os.path.join(os.path.dirname(__file__), file)

    with open(file_abspath) as f:
        stack_list = []
        line = f.readline()
        while line != '\n':
            l = line.rstrip('\n')
            tmp = [ l[i:i+4].strip('[] ') for i in range(0, len(l), 4)]
            stack_list.append(tmp)
            line = f.readline()
        else:
            crates_stack_map = { int(i) : [] for i in stack_list.pop()}

            while len(stack_list) :

                for i, val in enumerate(stack_list.pop()):
                    if len(val):
                        crates_stack_map[i+1].append(val)
        
        for line in f:
            tmp = line.replace('move ','').replace('from ','').replace('to ','').split()
            step = tuple([ int(_) for _ in tmp])
            procedure_steps.append(step)
        
def move_single( quantity, src, dest):
    ''' Define move '''
    while quantity:
        crates_stack_map[dest].append(crates_stack_map[src].pop())
        quantity = quantity-1

def move_multiple( quantity, src, dest):
    ''' Define move '''
    crates_stack_map[dest].extend(crates_stack_map[src][-quantity:])
    del crates_stack_map[src][-quantity:]

def do_part1(file):
    ''' Part 1 Solution '''
    load_input(file)

    for step in procedure_steps:
        quantity, src, dest = step
        move_single(quantity, src, dest)

    msg = ''
    for k, val in crates_stack_map.items():
        msg = msg + val[len(val)-1]
    
    return msg

def do_part2(file):
    ''' Part 2 Solution '''
    load_input(file)

    for step in procedure_steps:
        quantity, src, dest = step
        move_multiple(quantity, src, dest)

    msg = ''
    for k, val in crates_stack_map.items():
        msg = msg + val[len(val)-1]
    
    return msg

if __name__ == '__main__':
    print('Part 1 Sol : ', do_part1('input.txt'))
    print('Part 2 Sol : ', do_part2('input.txt'))