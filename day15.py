# http://adventofcode.com/2017/day/15

# ==== Part 1 ====

class Generator(object):
    def __init__(self, seed, factor, multiples_of=1):
        self.value = seed
        self.factor = factor
        self.multiples_of = multiples_of

    def next(self):
        self.value = (self.value * self.factor) % 2147483647
        if self.value % self.multiples_of != 0:
            return self.next()

        return self.value


def dueling_generators(seed_a, seed_b, pairs):
    gen_a = Generator(seed_a, factor=16807)
    gen_b = Generator(seed_b, factor=48271)

    matches = 0
    for _ in range(pairs):
        if judge(gen_a.next(), gen_b.next()):
            matches += 1

    return matches


def judge(decimal_a, decimal_b):
    binary_a = format(decimal_a, '032b')
    binary_b = format(decimal_b, '032b')
    return binary_a[-16:] == binary_b[-16:]


# print dueling_generators(seed_a=65, seed_b=8921, pairs=5)
# print dueling_generators(seed_a=783, seed_b=325, pairs=40000000)

# ==== Part 2 ====


def dueling_generators_2(seed_a, seed_b, pairs):
    gen_a = Generator(seed_a, factor=16807, multiples_of=4)
    gen_b = Generator(seed_b, factor=48271, multiples_of=8)

    matches = 0
    for _ in range(pairs):
        if judge(gen_a.next(), gen_b.next()):
            matches += 1

    return matches


print dueling_generators_2(seed_a=783, seed_b=325, pairs=5000000)
