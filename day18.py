# http://adventofcode.com/2017/day/18
import re
import threading
from Queue import Queue, Empty
from collections import defaultdict


# ==== Part 1 ====


def duet(input):
    instructions = parse(input)
    return run_instructions(instructions)


def parse(input):
    instructions = []
    for line in input.splitlines():
        p = re.compile('(\w+) (\w) ?([\w-]+)?')
        m = p.match(line)
        inst, reg, value = m.groups()
        instructions.append((inst, reg, value))
    return instructions


def run_instructions(instructions):
    registers = defaultdict(int)
    last_played_sound = None

    i = 0
    while 0 <= i < len(instructions):
        inst, x, y = instructions[i]

        if inst == 'snd':
            last_played_sound = registers[x]
        elif inst == 'set':
            registers[x] = get(y, registers)
        elif inst == 'add':
            registers[x] += get(y, registers)
        elif inst == 'mul':
            registers[x] *= get(y, registers)
        elif inst == 'mod':
            registers[x] %= get(y, registers)
        elif inst == 'rcv':
            if registers[x] != 0:
                return last_played_sound
        elif inst == 'jgz':
            if get(x, registers) > 0:
                i += get(y, registers)
                continue

        i += 1
    return None


def get(value, registers):
    return registers[value] if value.isalpha() else int(value)


example_input = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

# puzzle_input = open('day18.txt').read()
# recovered_freq = duet(puzzle_input)
# print "Recovered frequency: " + str(recovered_freq)


# ==== Part 2 ====

queue0 = Queue()
queue1 = Queue()


class Program(threading.Thread):

    def __init__(self, id, instructions, own_queue, other_queue):
        threading.Thread.__init__(self)
        self.id = id
        self.instructions = instructions
        self.own_queue = own_queue
        self.other_queue = other_queue

    def run(self):
        print "Program " + str(self.id) + ": started"
        messages_sent = run_instructions_2(self.id, self.instructions, self.own_queue, self.other_queue)
        print "Program " + str(self.id) + ": sent " + str(messages_sent) + " messages"
        print "Program " + str(self.id) + ": stopped"


def duet_2(input):
    instructions = parse(input)

    thread0 = Program(0, instructions, queue0, queue1)
    thread1 = Program(1, instructions, queue1, queue0)

    thread0.start()
    thread1.start()

    thread0.join()
    thread1.join()


def run_instructions_2(program_id, instructions, own_queue, other_queue):
    registers = defaultdict(int)
    registers['p'] = program_id
    messages_sent = 0

    i = 0
    while 0 <= i < len(instructions):
        inst, x, y = instructions[i]

        if inst == 'snd':
            other_queue.put(get(x, registers))
            messages_sent += 1
        elif inst == 'set':
            registers[x] = get(y, registers)
        elif inst == 'add':
            registers[x] += get(y, registers)
        elif inst == 'mul':
            registers[x] *= get(y, registers)
        elif inst == 'mod':
            registers[x] %= get(y, registers)
        elif inst == 'rcv':
            try:
                y = own_queue.get(block=True, timeout=5)
            except Empty:
                # Probably a deadlock, we'll stop right here
                break
            registers[x] = y
        elif inst == 'jgz':
            if get(x, registers) > 0:
                i += get(y, registers)
                continue

        i += 1
    return messages_sent


example_input_2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

puzzle_input = open('day18.txt').read()
duet_2(puzzle_input)
