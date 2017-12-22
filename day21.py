# http://adventofcode.com/2017/day/21
import math


def fractal_art(input, iterations):
    rules = parse(input)

    grid = [['.', '#', '.'],
            ['.', '.', '#'],
            ['#', '#', '#']]

    for _ in range(iterations):
        size = len(grid)
        square_width = 2 if size % 2 == 0 else 3

        converted_squares = convert_squares(grid, rules, square_width)
        grid = create_grid(converted_squares)

    return count_pixels(grid)


def parse(input):
    rules = {}
    for line in input.splitlines():
        split = line.split(' => ')
        input_pattern = [[x for x in row] for row in split[0].split('/')]
        output_pattern = [[x for x in row] for row in split[1].split('/')]
        rules[str(input_pattern)] = output_pattern
    return rules


def convert_squares(grid, rules, square_width):
    result = []
    grid_width = len(grid)
    for y in range(0, grid_width, square_width):
        for x in range(0, grid_width, square_width):
            square = create_square(x, y, grid, square_width)
            converted_square = convert_square(square, rules)
            result.append(converted_square)
    return result


def create_square(grid_column, grid_row, grid, square_width):
    square = [[] for _ in range(square_width)]
    for square_row in range(square_width):
        square[square_row] = grid[grid_row + square_row][grid_column: grid_column + square_width]
    return square


def convert_square(square, rules):
    pattern = str(square)
    if pattern in rules:
        return rules[pattern]

    flipped_pattern = str(flip(square))
    if flipped_pattern in rules:
        return rules[flipped_pattern]

    return convert_square(rotate(square), rules)


def create_grid(squares):
    squares_per_row = int(math.sqrt(len(squares)))
    square_width = len(squares[0])
    grid = [[] for _ in range(squares_per_row * square_width)]

    for idx, square in enumerate(squares):
        grid_row = (idx / squares_per_row) * square_width
        for square_row in range(square_width):
            grid[grid_row + square_row] += square[square_row]

    return grid


def count_pixels(grid):
    pixels = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                pixels += 1
    return pixels


def rotate(grid):
    return map(list, zip(*grid[::-1]))


def flip(grid):
    return [row[::-1] for row in grid]


# example_input = """../.# => ##./#../...
# .#./..#/### => #..#/..../..../#..#"""

puzzle_input = open('day21.txt').read()

pixels = fractal_art(puzzle_input, 5)
# pixels = fractal_art(puzzle_input, 18)
print pixels
