# http://adventofcode.com/2017/day/10

# ==== Part 1 ====

def knot_hash(input):
    list = range(256)
    pos = skip_size = 0

    lengths = [int(l) for l in input.split(',')]
    hash(list, lengths, pos, skip_size)

    return list[0] * list[1]


def hash(list, lengths, pos, skip_size):
    for length in lengths:
        if length > 1:
            reverse_sublist(pos, length, list)

        pos = (pos + length + skip_size) % len(list)
        skip_size += 1
    return pos, skip_size


def reverse_sublist(pos, length, list):
    end = (pos + length) % len(list)
    if end <= pos:
        sublist = list[pos:] + list[:end]
    else:
        sublist = list[pos:end]

    for idx, value in enumerate(reversed(sublist)):
        list[(pos + idx) % len(list)] = value


# puzzle_input = "183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88"
# print knot_hash(puzzle_input)


# ==== Part 2 ====

def knot_hash_2(input):
    sparse_hash = range(256)
    pos = skip_size = 0

    bytes = map(ord, input)
    bytes.extend([17, 31, 73, 47, 23])

    for _ in range(64):
        pos, skip_size = hash(sparse_hash, bytes, pos, skip_size)

    return to_hex_string(to_dense_hash(sparse_hash))


def to_dense_hash(sparse_hash):
    result = []
    BLOCK_SIZE = 16
    for i in range(0, 256, BLOCK_SIZE):
        block = sparse_hash[i:i + BLOCK_SIZE]
        result.append(reduce(lambda x, y: x ^ y, block))
    return result


def to_hex_string(dense_hash):
    return ''.join(map(lambda x: format(x, '02x'), dense_hash))


# example_input = "AoC 2017"
# example_input = "1,2,4"
# print knot_hash_2(puzzle_input)
