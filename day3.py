# http://adventofcode.com/2017/day/3

from collections import defaultdict

# ==== Part 1 ====

# input = 12
# input = 23
# input = 1024
input = 325489


def spiral_memory(number):
    x = y = 0
    dx, dy = 1, 0

    # The amount of steps we take before changing direction
    step_distance = 1
    steps = 0

    for i in range(1, number):
        if steps == step_distance:
            # Change direction
            dx, dy = -dy, dx

            if dx != 0:
                # Going left or right increases the step distance
                step_distance += 1

            steps = 0

        x, y = x + dx, y + dy
        steps += 1

    return calculate_manhattan_distance((x, y), (0, 0))


def calculate_manhattan_distance(p, q):
    (p1, p2) = p
    (q1, q2) = q
    return abs(p1 - q1) + abs(p2 - q2)


print spiral_memory(input)


# ==== Part 2 ====


def spiral_memory_2(number):
    x = y = 0
    dx, dy = 1, 0

    # A dictionary that stores square values. Other squares can use it to
    # calculate the sum of their adjacent squares
    squares = defaultdict(int)
    squares[0, 0] = 1

    # The amount of steps we take before changing direction
    step_distance = 1
    steps = 0

    value = 0
    while value < number:
        if steps == step_distance:
            # Change direction
            dx, dy = -dy, dx

            if dx != 0:
                # Going left or right increases the step distance
                step_distance += 1

            steps = 0

        x, y = x + dx, y + dy
        steps += 1

        value = sum_of_adjacent_squares(x, y, squares)
        squares[x, y] = value

    return value


def sum_of_adjacent_squares(x, y, squares):
    return squares[x - 1, y + 1] + squares[x, y + 1] + squares[x + 1, y + 1] + \
           squares[x - 1, y    ]                     + squares[x + 1, y    ] + \
           squares[x - 1, y - 1] + squares[x, y - 1] + squares[x + 1, y - 1]


print spiral_memory_2(input)
