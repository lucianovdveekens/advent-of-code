# http://adventofcode.com/2017/day/9


def stream_processing(chars):
    score = depth = garbage_counter = 0
    processing_garbage = False

    stream = iter(chars)
    for char in stream:
        if processing_garbage:
            if char is '>':
                processing_garbage = False
            elif char is '!':
                next(stream)
            else:
                garbage_counter += 1
        else:
            if char is '<':
                processing_garbage = True
            elif char is '{':
                depth += 1
                score += depth
            elif char is '}':
                depth -= 1

    return score, garbage_counter


puzzle_input = open('day9.txt').read()
score, garbage_counter = stream_processing(puzzle_input)
print score, garbage_counter
