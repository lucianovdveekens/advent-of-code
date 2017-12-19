# http://adventofcode.com/2017/day/19

# ==== Part 1 ====


def series_of_tubes(input):
    board = parse(input)
    position = find_start_position(board)

    steps = 0
    direction = (0, 1)
    letters = []

    while True:
        (x, y) = position
        value = board[y][x]

        if value == ' ':
            break
        elif value == '+':
            direction = change_direction(x, y, board, direction)
        elif value.isalpha():
            letters.append(value)

        (dx, dy) = direction
        position = (x + dx, y + dy)
        steps += 1

    return letters, steps


def find_start_position(board):
    position = ()
    for idx, char in enumerate(board[0]):
        if char == '|':
            position = (idx, 0)
    return position


def parse(input):
    board = []
    for line in input.splitlines():
        row = list(line)
        board.append(row)
    return board


def change_direction(x, y, board, direction):
    (dx, dy) = direction
    previous_pos = (x - dx, y - dy)

    if y - 1 >= 0 and (x, y - 1) != previous_pos and board[y - 1][x] != ' ':
        return 0, -1
    elif x + 1 < len(board[y]) and (x + 1, y) != previous_pos and board[y][x + 1] != ' ':
        return 1, 0
    elif y + 1 < len(board) and (x, y + 1) != previous_pos and board[y + 1][x] != ' ':
        return 0, 1
    elif x - 1 >= 0 and (x - 1, y) != previous_pos and board[y][x - 1] != ' ':
        return -1, 0


example_input = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""

# puzzle_input = open('day19.txt').read()
# letters, _ = series_of_tubes(puzzle_input)
# print "".join(letters)

# ==== Part 2 ====

puzzle_input = open('day19.txt').read()
_, steps = series_of_tubes(puzzle_input)
print steps
