import os
import re
from collections import deque
import operator
from functools import reduce

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def get_list_lcm(your_list):
    return reduce(lambda x, y: lcm(x, y), your_list)

def makeoperation(oper, n=None):

    if oper == '*':
        if n == None:
            return lambda x: operator.imul(x,x)
        else:
            return lambda x: operator.imul(x,n)
    elif oper == '+':
        if n == None:
            return lambda x: operator.iadd(x,x)
        else:
            return lambda x: operator.iadd(x,n)

def maketest(i, n , m):

    def test(x):
        if operator.mod(x, i) == 0:
            return n
        else:
            return m
    return test

class Monkey:

    LCM = 1

    def __init__(self, items, op, test, grp):
        self._items = deque(items)
        self._opfunc = op
        self._testfunc = test
        self._group = grp
        self._inspect_cont = 0
    
    def perform_turn(self, relief=1):

        while len(self._items):
            item = self._items.popleft()
            # Inspect Item
            worry_level = self._opfunc(item)
            self._inspect_cont = self._inspect_cont + 1
            # apply Relief
            if relief:
                worry_level = worry_level // 3
            else:
                worry_level = worry_level % Monkey.LCM

            # Decide next Monekey to throw item
            next = self._testfunc(worry_level)

            # throw the item
            self._group[next]._items.append(worry_level)
   
    def __str__(self):
        return f'Monkey({self._inspect_cont})'

    def __repr__(self):
        return f'Monkey({self._inspect_cont})'

def load_input(file):
    ''' Load input into DS '''
    file_abspath =  os.path.join(os.path.dirname(__file__), file)
    
    denominator_list = []

    with open(file_abspath)  as f:

        monkeys = {}

        line = f.readline().strip()

        while len(line):
            # Read Monkey index
            line = line.strip()
            index = line[len(line)-2]

            # Read starting List
            line = f.readline().strip()
            items = [int(s) for s in re.findall(r'\b\d+\b',line)]

            # Read Operation
            line = f.readline().strip()
            tmp  = line.split('=')
            tmp  = [ _ for _ in tmp[1].strip().split(' ')]
            if tmp[2] == 'old':
                opfunc = makeoperation(tmp[1])
                opfunc_str = f'makeoperation({tmp[1]})'
            else:
                opfunc = makeoperation(tmp[1], int(tmp[2]))
                opfunc_str = f'makeoperation({tmp[1]}, {int(tmp[2])})'

            # Read Test
            line = f.readline().strip()
            tmp = [int(s) for s in re.findall(r'\b\d+\b',line)]
            i = tmp[0]

            line = f.readline().strip()
            tmp = [int(s) for s in re.findall(r'\b\d+\b',line)]
            n = tmp[0]

            line = f.readline().strip()
            tmp = [int(s) for s in re.findall(r'\b\d+\b',line)]
            m = tmp[0]

            testfunc = maketest(i, n, m)
            denominator_list.append(i)
            #print(f'Money {index} : {items} , {opfunc_str}, maketest({i},{n},{m}))')
            monkeys[int(index)] = Monkey(items, opfunc, testfunc, monkeys)
            line = f.readline()
            if len(line):
                line = f.readline()
    lcm = get_list_lcm(denominator_list)
    Monkey.LCM = lcm
    return monkeys

def do_part1(file):
    monkey_grp = load_input(file)
    for _ in range(0, 20):
        for i in monkey_grp.keys():
            monkey_grp[i].perform_turn()
    
    monkeys = monkey_grp.values()
    sorted_monkeys = sorted(monkeys, key= lambda x: x._inspect_cont)
    total = len(sorted_monkeys)
    return sorted_monkeys[total-1]._inspect_cont * sorted_monkeys[total-2]._inspect_cont

def do_part2(file):
    monkey_grp = load_input(file)
    for _ in range(0, 10000):
        for i in monkey_grp.keys():
            monkey_grp[i].perform_turn(relief=0)
    
    monkeys = monkey_grp.values()
    sorted_monkeys = sorted(monkeys, key= lambda x: x._inspect_cont)
    print(sorted_monkeys)
    total = len(sorted_monkeys)
    return sorted_monkeys[total-1]._inspect_cont * sorted_monkeys[total-2]._inspect_cont

if __name__ == '__main__':
    #print(f'Part 1 Sol: ', do_part1('input.txt'))
    print(f'Part 2 Sol: ', do_part2('input.txt'))