# http://adventofcode.com/2017/day/8
import operator
import re
from collections import defaultdict

example = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

ops = {">": operator.gt, "<": operator.lt, "==": operator.eq,
       ">=": operator.ge, "<=": operator.le, "!=": operator.ne,
       "inc": operator.add, "dec": operator.sub}


def run_instructions(input):
    registers = defaultdict(int)
    highest_held_value = 0

    p = re.compile(r'(\w+) (inc|dec) (-?\d+) if (\w+) ([><=!]+) (-?\d+)')

    for instruction in input.splitlines():
        m = p.match(instruction)
        reg, op, num, reg2, op2, num2 = m.groups()

        condition = ops[op2](registers[reg2], int(num2))

        if condition:
            value = registers[reg]
            new_value = ops[op](value, int(num))
            highest_held_value = max(new_value, highest_held_value)
            registers[reg] = new_value

    return registers, highest_held_value


input = open('day8.txt').read()
registers, highest_held_value = run_instructions(input)

print "Highest register value: {}".format(max(registers.values()))
print "Highest held register value: {}".format(highest_held_value)
