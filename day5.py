# http://adventofcode.com/2017/day/5

# ==== Part 1 ====

example = """0
3
0
1 
-3"""


def cpu_jumps(input):
    offsets = [int(line) for line in input.splitlines()]

    idx = 0
    count = 0

    while 0 <= idx < len(offsets):
        offset = offsets[idx]
        offsets[idx] = offset + 1
        idx += offset
        count += 1

    return count


# input = open('day5.txt').read()
# print cpu_jumps(input)


# ==== Part 2 ====

def cpu_jumps_2(input):
    offsets = [int(line) for line in input.splitlines()]

    idx = 0
    count = 0

    while 0 <= idx < len(offsets):
        offset = offsets[idx]
        if offset >= 3:
            offsets[idx] = offset - 1
        else:
            offsets[idx] = offset + 1
        idx += offset
        count += 1

    return count


input = open('day5.txt').read()
print cpu_jumps_2(input)
