import os

class Tree:
    
    def __init__(self, height) -> None:
        self.height = height
        self._visibility = None
        self._scenic_score = None
    
    @property
    def visibility(self):
        return self._visibility
    
    @visibility.setter
    def visibility(self, flag):
        self._visibility = flag
    
    @property
    def scenic_score(self):
        return self._scenic_score
    
    @scenic_score.setter
    def scenic_score(self, flag):
        self._scenic_score = flag
    
    def __str__(self):
        return f'({self.height}, {self.visibility}, {self.scenic_score})'
    
    def __repr__(self):
        return f'({self.height}, {self.visibility}, {self.scenic_score})'

class TreeGrid:

    def __init__(self, inp) -> None:
        self.grid = [[ Tree(col) for col in row] for row in inp]
        self.row_max = len(inp)
        self.col_max = len(inp[0])
    
    def detect_visibility(self):
        
        # check row-wise
        for row in range(0, self.row_max):
            
            self.grid[row][0].visibility  = 1
            level = self.grid[row][0].height
            # left-view
            for col in range(1, self.col_max):
                if level == 9:
                    break
                tree = self.grid[row][col]
                if tree.height > level:
                    tree.visibility = 1
                    level = tree.height

            # right-view
            self.grid[row][self.col_max-1].visibility  = 1
            level = self.grid[row][self.col_max-1].height
            for col in reversed(range(1, self.col_max)):
                if level == 9:
                    break
                tree = self.grid[row][col]
                if tree.height > level:
                    tree.visibility = 1
                    level = tree.height
        
        # check col-wise
        for col in range(0, self.col_max):
            
            self.grid[0][col].visibility  = 1
            level = self.grid[0][col].height
            # up-view
            for row in range(1, self.row_max):
                if level == 9:
                    break
                tree = self.grid[row][col]
                if tree.height > level:
                    tree.visibility = 1
                    level = tree.height

            # down-view
            self.grid[self.row_max-1][col].visibility  = 1
            level = self.grid[self.row_max-1][col].height
            for row in reversed(range(1, self.row_max)):
                if level == 9:
                    break
                tree = self.grid[row][col]
                if tree.height > level:
                    tree.visibility = 1
                    level = tree.height
            
        count = 0

        for i in range(self.row_max):
            for j in range(self.col_max):
                if self.grid[i][j].visibility != None:
                    count = count + 1
        
        return count

    def calculate_scenic_score(self):

        max_scenic = 0

        for row in range(self.row_max):
            for col in range(self.col_max):
                
                level = self.grid[row][col].height

                #Left Score
                left_score = 0
                for _ in reversed(range(0,col)):
                    curr_tree = self.grid[row][_]
                    left_score = left_score + 1
                    if curr_tree.height >= level:
                        break

                #Right Score
                right_score = 0
                for _ in range(col+1,self.col_max):
                    curr_tree = self.grid[row][_]
                    right_score = right_score + 1
                    if curr_tree.height >= level:
                        break
                
                #Up Score
                up_score = 0
                for _ in reversed(range(0,row)):
                    curr_tree = self.grid[_][col]
                    up_score = up_score + 1
                    if curr_tree.height >= level:
                        break

                #down Score
                down_score = 0
                for _ in range(row+1,self.row_max):
                    curr_tree = self.grid[_][col]
                    down_score = down_score + 1
                    if curr_tree.height >= level:
                        break
                total_score = left_score * right_score * up_score * down_score
                self.grid[row][col].scenic_score = total_score

                if total_score > max_scenic:
                    max_scenic = total_score
        
        return max_scenic

    def __str__(self):
        return str(self.grid)

def load_input(file):
    ''' Load input into DS '''
    file_abspath =  os.path.join(os.path.dirname(__file__), file)
    input = []
    with open(file_abspath)  as f:
        input = [ [int(_) for _ in line.strip()] for line in f ]
    
    return input

def do_part1(file):
    ''' Part 1 Solution '''
    quadcoper_inp = load_input(file)
    treegrid = TreeGrid(quadcoper_inp)

    return treegrid.detect_visibility()

def do_part2(file):
    ''' Part 2 Solution '''
    quadcoper_inp = load_input(file)
    treegrid = TreeGrid(quadcoper_inp)
    return treegrid.calculate_scenic_score()
    
if __name__ == '__main__':
    print(f' Part 1 Sol : {do_part1("input.txt")}')
    print(f' Part 2 Sol : {do_part2("input.txt")}')