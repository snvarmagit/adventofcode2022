import os

class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def moveright(self):
        self.x = self.x + 1
        return self.get_position()

    def moveleft(self):
        self.x = self.x - 1
        return self.get_position()

    def moveup(self):
        self.y = self.y + 1
        return self.get_position()

    def movedown(self):
        self.y = self.y - 1
        return self.get_position()

    def movediagonal(self, pos):
        chgx, chgy = pos
        self.x = self.x + chgx
        self.y = self.y + chgy
        return self.get_position()

    def get_position(self):
        return self.x, self.y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

class Rope:
    def __init__(self, tail_count=1) -> None:
        self._head = Position(0,0)
        self._tails = dict()
        for i in range(1, tail_count+1):
            self._tails[i] = Position(0,0)

        self.tail_pos = { self._tails[tail_count].get_position() }
    
    def perform_motion(self, input):
        
        action, steps = input

        for _ in range(steps):
           
            if action == 'R':
                self._head.moveright()
            elif action == 'L':
                self._head.moveleft()
            elif action == 'U':
                self._head.moveup()
            elif action == 'D':
                self._head.movedown()
            
            head = self._head

            for tail in self._tails.values():

                newh_x, newh_y = head.get_position()
                tail_x, tail_y = tail.get_position()
                
                diff_x = abs(newh_x - tail_x)
                diff_y = abs(newh_y - tail_y)
                
                tmp = diff_x, diff_y
                if tmp in {(0,0), (1,0), (0,1), (1,1)}:
                    head = tail
                    continue
                elif newh_x != tail_x and newh_y != tail_y:
                    chg_x , chg_y = 1 , 1
                    if newh_x < tail_x:
                        chg_x = -1
                    if newh_y < tail_y:
                        chg_y = -1
                    pos = chg_x , chg_y
                    tail_x, tail_y = tail.movediagonal(pos)
                elif newh_x == tail_x:
                    if newh_y < tail_y:
                        tail_x, tail_y = tail.movedown()
                    else:
                        tail_x, tail_y = tail.moveup()
                elif newh_y == tail_y:
                    if newh_x < tail_x:
                        tail_x, tail_y = tail.moveleft()
                    else:
                        tail_x, tail_y = tail.moveright()
                head = tail

            pos = tail.get_position()
            self.tail_pos.add(pos)

def load_input(file):
    ''' Load input into DS '''
    file_abspath =  os.path.join(os.path.dirname(__file__), file)
    input = []
    with open(file_abspath)  as f:
        for line in f:
            action, steps = line.strip().split(' ')
            tmp = action, int(steps)
            input.append(tmp)
    return input

def do_part1(file):
    inp = load_input(file)
    rope = Rope()
    for action in inp:
        rope.perform_motion(action)
    return len(rope.tail_pos)

def do_part2(file):
    inp = load_input(file)
    rope = Rope(9)
    for action in inp:
        rope.perform_motion(action)
    return len(rope.tail_pos)

if __name__ == '__main__':
    print(f' Part 1 Sol: {do_part1("input.txt")}')
    print(f' Part 2 Sol: {do_part2("input.txt")}')