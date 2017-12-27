# http://adventofcode.com/2017/day/22

from collections import defaultdict


def sporifica_virus(input, bursts):
    infections_caused = 0
    current_pos = (0, 0)
    direction = (0, 1)

    map = create_map(input)

    for _ in range(bursts):
        node = map[current_pos]
        direction = turn(node, direction)

        if node == '.':
            map[current_pos] = '#'
            infections_caused += 1
        else:
            map[current_pos] = '.'

        (x, y) = current_pos
        (dx, dy) = direction
        current_pos = (x + dx, y + dy)

    return infections_caused


def create_map(input):
    map = defaultdict(lambda: '.')

    lines = input.splitlines()
    center = (len(lines) / 2, len(lines) / 2)
    for row in range(len(lines)):
        for col, node in enumerate(lines[row]):
            (cx, cy) = center
            # The position is relative to the center
            relative_pos = (col - cx, cy - row)
            map[relative_pos] = node

    return map


def turn(node, direction):
    """ Turn right or left based on whether the node is infected or not """
    (dx, dy) = direction

    sgn = 1
    if dy != 0:
        sgn = -1
    if node == '#':
        sgn = -sgn

    return sgn * dy, sgn * dx


# example_input = """..#
# #..
# ..."""
# puzzle_input = open('day22.txt').read()
# infections_caused = sporifica_virus(puzzle_input, bursts=10000)
# print infections_caused


# ==== Part 2 ====

def sporifica_virus_2(input, bursts):
    infections_caused = 0
    current_pos = (0, 0)
    direction = (0, 1)

    map = create_map(input)

    for _ in range(bursts):
        node = map[current_pos]

        if node == '.':
            direction = turn(node, direction)
            map[current_pos] = 'W'
        elif node == 'W':
            map[current_pos] = '#'
            infections_caused += 1
        elif node == '#':
            direction = turn(node, direction)
            map[current_pos] = 'F'
        elif node == 'F':
            (dx, dy) = direction
            direction = (-dx, -dy)
            map[current_pos] = '.'

        (x, y) = current_pos
        (dx, dy) = direction
        current_pos = (x + dx, y + dy)

    return infections_caused


# example_input = """..#
# #..
# ..."""
puzzle_input = open('day22.txt').read()
infections_caused = sporifica_virus_2(puzzle_input, bursts=10000000)
print infections_caused
