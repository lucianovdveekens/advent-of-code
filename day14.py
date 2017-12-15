# http://adventofcode.com/2017/day/14
import day10


# ==== Part 1 ====

def disk_defragmentation(key):
    grid = [[0 for x in range(128)] for y in range(128)]
    for row in range(128):
        input = key + "-" + str(row)
        output = day10.knot_hash_2(input)

        for char_idx, char in enumerate(output):
            decimal = int(char, 16)
            binary = format(decimal, '04b')
            for bit_idx, bit in enumerate(binary):
                grid[row][char_idx * 4 + bit_idx] = int(bit)

    grid_sum = 0
    for row in grid:
        grid_sum += sum(row)

    return grid_sum


example_key = "flqrgnkx"
puzzle_input = "hxtvlmkl"
# print disk_defragmentation(example_key)


# ==== Part 2 ====


def mark_cell(col, row, grid, region):
    if 0 <= col < 128 and 0 <= row < 128 and grid[row][col] == '#':
        grid[row][col] = str(region)
        mark_cell(col, row - 1, grid, region)
        mark_cell(col + 1, row, grid, region)
        mark_cell(col, row + 1, grid, region)
        mark_cell(col - 1, row, grid, region)


def disk_defragmentation_2(key):
    grid = [['' for x in range(128)] for y in range(128)]
    for row in range(128):
        input = key + "-" + str(row)
        output = day10.knot_hash_2(input)

        for char_idx, char in enumerate(output):
            decimal = int(char, 16)
            binary = format(decimal, '04b')
            for bit_idx, bit in enumerate(binary):
                grid[row][char_idx * 4 + bit_idx] = '#' if bit == '1' else '.'

    region = 0
    for row_idx, row in enumerate(grid):
        for col_idx, value in enumerate(row):
            if value == '#':
                region += 1
                mark_cell(col_idx, row_idx, grid, region)

    return region


print disk_defragmentation_2(puzzle_input)
