import os
from collections import deque

SYSTEM_SIZE = 70000000
UPDATE_SIZE = 30000000


class Directory():
    ''' Represent Directory '''
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.children = {}
        self.total_size = -1

class File():
    ''' Represent File '''
    def __init__(self, size, name) -> None:
        self.name = name
        self.size = size

def load_input(file):
    ''' Create N-array Tree structure '''
    root = Directory('/')

    file_abspath =  os.path.join(os.path.dirname(__file__), file)
    current = None
    with open(file_abspath) as f:
        for line in f:
            ln = line.strip()

            if ln.startswith('$'):
                cmd = ln.lstrip('$ ').split()
                if cmd[0] == 'cd':
                    name = cmd[1]
                    if name == '/':
                        current = root
                    elif name == '..':
                        current = current.parent
                    else:
                        current = current.children[name]
                elif cmd[0] == 'ls':
                    pass
            else:
                if ln.startswith('dir'):
                    _ , name = ln.split()
                    current.children[name] = Directory(name, current)
                else:
                    size, name = ln.split()
                    current.children[name] = File(int(size), name)
    return root

def calculate_dir_size(node):
    ''' Calculate directory size '''
    node.total_size  = 0
    for item in node.children.values():
        if isinstance(item, File):
            node.total_size = node.total_size + item.size
        elif isinstance(item, Directory):
            node.total_size = node.total_size + calculate_dir_size(item)
    return node.total_size

def find_list_atmost_dirs(node, max_size):
    result_dir = []

    queue = []
    queue.append(node)

    while len(queue):

        current = queue.pop()

        if current.total_size <= max_size:
            result_dir.append(current)

        for sub_dir in current.children.values():
            if isinstance(sub_dir, Directory):
                queue.append(sub_dir)
    
    return [ _.total_size for _ in result_dir]

def find_list_atleast_dirs(node, min_size):
    result_dir = []

    queue = []
    queue.append(node)

    while len(queue):

        current = queue.pop()

        if current.total_size >= min_size:
            result_dir.append(current)

        for sub_dir in current.children.values():
            if isinstance(sub_dir, Directory):
                queue.append(sub_dir)
    
    return [ _.total_size for _ in result_dir]

def do_part1(file):
    ''' Part 1 Solution '''
    root = load_input(file)
    calculate_dir_size(root)
    result_dir = find_list_atmost_dirs(root, 100000)
    return sum(result_dir)

def do_part2(file):
    ''' Part 2 Solution '''
    root = load_input(file)
    calculate_dir_size(root)
    unused_size = SYSTEM_SIZE - root.total_size
    min_size = UPDATE_SIZE - unused_size
    result_dir = find_list_atleast_dirs(root, min_size)
    sort_list = sorted(result_dir)
    return sort_list[0]



if __name__ == '__main__':
    print('Part 1 Sol :', do_part1('input.txt'))
    print('Part 2 Sol :', do_part2('input.txt'))