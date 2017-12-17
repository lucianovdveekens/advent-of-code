# http://adventofcode.com/2017/day/16
import copy
import re


# ==== Part 1 ====

def permutation_promenade(input, programs):
    programs = list(programs)
    for dance_move in input.split(','):
        move_type = dance_move[0]
        move_value = dance_move[1:]

        if move_type == 's':
            programs = spin(move_value, programs)
        elif move_type == 'x':
            exchange(move_value, programs)
        elif move_type == 'p':
            partner(move_value, programs)

    return ''.join(programs)


def spin(move_value, programs):
    number = int(move_value)
    programs = programs[-number:] + programs[:-number]
    return programs


def partner(move_value, programs):
    p = re.compile('([a-z]+)/([a-z]+)')
    m = p.match(move_value)
    program_a, program_b = m.groups()
    pos_a = programs.index(program_a)
    pos_b = programs.index(program_b)
    programs[pos_a], programs[pos_b] = programs[pos_b], programs[pos_a]


def exchange(move_value, programs):
    p = re.compile('(\d+)/(\d+)')
    m = p.match(move_value)
    pos_a, pos_b = m.groups()
    pos_a, pos_b = int(pos_a), int(pos_b)
    programs[pos_a], programs[pos_b] = programs[pos_b], programs[pos_a]


# example_input = "s1,x3/4,pe/b"
# programs = [chr(x) for x in range(ord('a'), ord('e') + 1)]

puzzle_input = open('day16.txt').read()
programs = [chr(x) for x in range(ord('a'), ord('p') + 1)]
print permutation_promenade(puzzle_input, programs)


# ==== Part 2 ====

def permutation_promenade_2(input, programs):
    repeat_factor = find_repeat_factor(input, programs)

    for _ in xrange(1000000000 % repeat_factor):
        programs = permutation_promenade(input, programs)

    return programs


def find_repeat_factor(input, programs):
    original = copy.copy(programs)

    repeat_factor = 0
    while True:
        programs = permutation_promenade(input, programs)
        repeat_factor += 1
        if programs == original:
            break

    return repeat_factor


puzzle_input = open('day16.txt').read()
programs = ''.join([chr(x) for x in range(ord('a'), ord('p') + 1)])
print permutation_promenade_2(puzzle_input, programs)
