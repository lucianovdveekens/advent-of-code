# http://adventofcode.com/2017/day/13
import copy
import re

example_input = """0: 3
1: 2
4: 4
6: 4"""


# ==== Part 1 ====


class Layer(object):

    def __init__(self, depth, range):
        self.depth = depth
        self.list = [''] * range
        self.scanner_index = 0
        self.list[self.scanner_index] = 'S'
        self.speed = 1

    def _at_boundary(self, idx):
        return idx == 0 and self.speed == -1 or idx == len(self.list) - 1 and self.speed == 1

    def move_scanner(self):
        if self._at_boundary(self.scanner_index):
            self.speed = -self.speed

        self.list[self.scanner_index] = ''
        self.scanner_index += self.speed
        self.list[self.scanner_index] = 'S'

    def __repr__(self):
        return "<Layer depth=" + str(self.depth) + \
               ",list=" + str(self.list) + \
               ",direction=" + str(self.speed) + \
               ">"


def create_layers(input):
    layers = []
    for line in input.splitlines():
        p = re.compile('(\d+): (\d+)')
        m = p.match(line)
        depth, range = m.groups()
        layers.append(Layer(int(depth), int(range)))
    return layers


def move_scanners(layers):
    for layer in layers:
        layer.move_scanner()


def packet_scanner(input):
    severity = 0
    last_depth = 0

    layers = create_layers(input)
    for layer in layers:
        # Did we skip an empty layer?
        # If so, move the scanners to catch up.
        for _ in range(last_depth, layer.depth - 1):
            move_scanners(layers)

        if layer.list[0] == 'S':
            severity += layer.depth * len(layer.list)

        move_scanners(layers)

        last_depth = layer.depth

    return severity


puzzle_input = open('day13.txt').read()
print packet_scanner(puzzle_input)


# ==== Part 2 ====

def packet_scanner_2(input):
    delay = 0
    layers = create_layers(input)

    while True:
        print "Trying delay:", delay
        caught = False
        for idx, layer in enumerate(layers):
            copy_of_layer = copy.deepcopy(layer)

            for _ in range(layer.depth):
                copy_of_layer.move_scanner()

            if copy_of_layer.list[0] == 'S':
                caught = True
                break

        if not caught:
            return delay

        delay += 1
        move_scanners(layers)


print packet_scanner_2(example_input)
