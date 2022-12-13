import time
import os

class CPU:

    REGISTER = 1

    def __init__(self, start, freqncy) -> None:
        self._start = start
        self._freqncy = freqncy
        self._probe_list = []
        
    def exec_program(self, program):

        for command in program:
            if command == 'noop':
                self.cycle()
            elif command.startswith('addx'):
                _ , val = command.split(' ')
                self.cycle()
                self.cycle()
                CPU.REGISTER = CPU.REGISTER + int(val)
        
        return self._probe_list
           
    def probe(func):
        count = 0

        def wrapper(self):
            nonlocal count
            count = count + 1

            if count % self._freqncy == self._start:
                self._probe_list.append(self.REGISTER * count)

            return func(self)
        
        return wrapper
    
    @probe
    def cycle(self):
        time.sleep(0.01)

class CRT:

    REGISTER = 1

    def __init__(self, width) -> None:
        self._width = width
        
    def exec_program(self, program):

        for command in program:
            if command == 'noop':
                self.cycle()
            elif command.startswith('addx'):
                _ , val = command.split(' ')
                self.cycle()
                self.cycle()
                CRT.REGISTER = CRT.REGISTER + int(val)
           
    def display(func):
        cycle = 0

        def wrapper(self):
            nonlocal cycle
            cycle = cycle + 1

            pixel = (cycle % self._width) -1
            if pixel in self.get_sprite():
                print('#',end='')
            else:
                print('.',end='')
            
            if cycle % self._width == 0:
                print()

            return func(self)
        
        return wrapper
    
    @display
    def cycle(self):
        time.sleep(0.01)

    def get_sprite(self):
        return [CRT.REGISTER-1, CRT.REGISTER, CRT.REGISTER+1]

def load_input(file):
    ''' Load input into DS '''
    file_abspath =  os.path.join(os.path.dirname(__file__), file)
    input = []
    with open(file_abspath)  as f:
        for line in f:
            input.append(line.strip())
    return input

def do_part1(file):
    inp = load_input(file)

    probe = CPU(20,40)
    return sum(probe.exec_program(inp))


def do_part2(file):
    inp = load_input(file)

    display = CRT(40)
    display.exec_program(inp)

if __name__ == '__main__':
    print(f'Part 1 Sol: {do_part1("input.txt")}')
    do_part2('input.txt')