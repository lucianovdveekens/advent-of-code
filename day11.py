# http://adventofcode.com/2017/day/11


class Cube(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def distance(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y), abs(self.z - other.z))


directions = {
    'n': Cube(0, +1, -1),
    'ne': Cube(+1, 0, -1),
    'se': Cube(+1, -1, 0),
    's': Cube(0, -1, +1),
    'sw': Cube(-1, 0, +1),
    'nw': Cube(-1, +1, 0)
}

START_CUBE = Cube(0, 0, 0)


def hex_ed(input):
    cube = Cube(0, 0, 0)
    max_distance = 0

    steps = input.split(',')
    for step in steps:
        direction = directions[step]
        cube.add(direction)

        distance = cube.distance(START_CUBE)
        max_distance = max(distance, max_distance)

    return cube, max_distance


# ==== Part 1 ====

# example_input = "ne,ne,sw,sw"
puzzle_input = open('day11.txt').read()
cube, max_distance = hex_ed(puzzle_input)
print cube.distance(START_CUBE)

# ==== Part 2 ====
print max_distance
