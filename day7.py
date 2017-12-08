# http://adventofcode.com/2017/day/7
import random
import re

example = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


# ==== Part 1 ====

def recursive_circus(input):
    program_dict = {}

    pattern = re.compile(r'(\w+) \((\d+)\)( -> (.*))?')
    for line in input.splitlines():
        match = pattern.match(line)
        name, weight, _, other_programs = match.groups()

        program = program_dict.setdefault(name, Program(name))
        program.weight = int(weight)

        if other_programs is not None:
            program.towers = create_towers(program, other_programs, program_dict)

    random_program = random.choice(program_dict.values())
    return find_bottom(random_program)


def create_towers(disc_holder, programs, program_by_name):
    towers = []
    for name in programs.split(', '):
        program = program_by_name.setdefault(name, Program(name))
        program.parent = disc_holder
        towers.append(program)

    return towers


def find_bottom(node):
    return node if node.parent is None else find_bottom(node.parent)


class Program:
    def __init__(self, name, weight=None, towers=None, parent=None):
        self.name = name
        self.weight = weight
        self.towers = towers
        self.parent = parent

    def __repr__(self):
        return "<Program name=" + self.name + \
               ", weight=" + str(self.weight) + \
               ", parent=" + str(self.parent.name if self.parent else None) + \
               ", towers=" + str(self.towers) + \
               ">"


puzzle_input = open('day7.txt').read()
bottom = recursive_circus(puzzle_input)
print "Bottom program: " + bottom.name


# ==== Part 2 ====

def find_unbalanced_disc(program):
    towers = program.towers
    if towers is None:
        return
    
    disc = []
    for tower in towers:
        result = find_unbalanced_disc(tower)
        if result is not None:
            return result

        disc.append((tower, sum_weights(tower)))

    if not in_balance(disc):
        return disc


def sum_weights(program):
    sum = program.weight

    towers = program.towers
    if towers is not None:
        for tower in towers:
            sum += sum_weights(tower)

    return sum


def in_balance(disc):
    return all(weight == disc[0][1] for _, weight in disc)


disc = find_unbalanced_disc(bottom)

print "Unbalanced disc:"
for tower, weight in disc:
    print "{} ({}) = {}".format(tower.name, tower.weight, weight)
