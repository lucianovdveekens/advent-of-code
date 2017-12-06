# http://adventofcode.com/2017/day/6

example = "0 2 7 0"
puzzle_input = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"


def memory_reallocation(banks):
    history = []
    cycles = 0

    while banks not in history:
        history.append(list(banks))

        idx, blocks = max(enumerate(banks), key=lambda x: x[1])
        banks[idx] = 0

        while blocks > 0:
            idx = (idx + 1) % len(banks)
            banks[idx] += 1
            blocks -= 1

        cycles += 1

    return cycles, banks


# ==== Part 1 ====
banks = [int(bank) for bank in puzzle_input.split()]
cycles, final_state = memory_reallocation(banks)
print cycles

# ==== Part 2 ====
cycles, _ = memory_reallocation(final_state)
print cycles
