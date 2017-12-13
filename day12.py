# http://adventofcode.com/2017/day/12
import re

example_input = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""


# ==== Part 1 ====

def digital_plumber(input):
    dict = create_dict(input)

    group = set()
    follow_pipes(0, dict, group)

    return group


def create_dict(input):
    dict = {}
    for line in input.splitlines():
        p = re.compile('(\d+) <-> ([\d, ]+)')
        m = p.match(line)
        id, programs = m.groups()

        dict[int(id)] = [int(p) for p in programs.split(',')]
    return dict


def follow_pipes(id, dict, group):
    for program in dict[id]:
        if program in group:
            continue
        group.add(program)
        follow_pipes(program, dict, group)


puzzle_input = open('day12.txt').read()
group = digital_plumber(puzzle_input)
print len(group)


# ==== Part 2 ====

def digital_plumber_2(input):
    dict = create_dict(input)
    groups = 0

    visited = set()
    for id in dict.keys():
        if id not in visited:
            follow_pipes(id, dict, visited)
            groups += 1

    return groups


groups = digital_plumber_2(puzzle_input)
print groups
