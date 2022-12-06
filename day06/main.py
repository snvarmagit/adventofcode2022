import os
from collections import deque

def get_inp_stream(file):
    ''' Get Input stream '''
    file_abspath =  os.path.join(os.path.dirname(__file__), file)
    f = open(file_abspath, mode='r', encoding='utf-8')
    return f

def find_start_of_packet(f, size):
    protocol_buf = deque(maxlen=size)

    for _ in range(1, size):
        protocol_buf.append(f.read(1))

    count = size -1

    c = f.read(1)
    while c != '\n':
        count = count + 1
        protocol_buf.append(c)

        if len(set(protocol_buf)) == size:
            break
        else:
            c = f.read(1)
    else:
        count = -1
    
    return count

def do_part1(file):
    ''' Part 1 Soluton '''
    inp_stream = get_inp_stream(file)
    count = find_start_of_packet(inp_stream, 4)
    inp_stream.close()
    return count

def do_part2(file):
    ''' Part 2 Soluton '''
    inp_stream = get_inp_stream(file)
    count = find_start_of_packet(inp_stream, 14)
    inp_stream.close()
    return count

if __name__ == '__main__':
    print('Part 1 Sol: ', do_part1('input.txt'))
    print('Part 2 Sol: ', do_part2('input.txt'))