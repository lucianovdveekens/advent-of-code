# http://adventofcode.com/2017/day/23
from collections import defaultdict
from math import sqrt

from day18 import value_of, parse


def coprocessor_conflagration(input):
    instructions = parse(input)
    registers = defaultdict(int)

    return run_instructions(instructions, registers)


def run_instructions(instructions, registers):
    multiplications = 0

    i = 0
    while 0 <= i < len(instructions):
        inst, x, y = instructions[i]

        if inst == 'set':
            registers[x] = value_of(y, registers)
        elif inst == 'sub':
            registers[x] -= value_of(y, registers)
        elif inst == 'mul':
            registers[x] *= value_of(y, registers)
            multiplications += 1
        elif inst == 'jnz':
            if value_of(x, registers) != 0:
                i += value_of(y, registers)
                continue

        i += 1
    return multiplications


puzzle_input = open('day23.txt').read()
print coprocessor_conflagration(puzzle_input)


# ==== Part 2 ====

def coprocessor_conflagration_2():
    h = 0

    b = 109300
    c = 126300

    for b in range(109300, c + 1, 17):
        if not prime(b):
            h += 1

    return h


def prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


print coprocessor_conflagration_2()
