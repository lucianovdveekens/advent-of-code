# http://adventofcode.com/2017/day/17

# ==== Part 1 ====
from blist._blist import blist


def spinlock(steps, insertions):
    # 'blist' improves the performance of list insertion
    lst = blist([0])

    value = 1
    pos = 0
    for _ in xrange(insertions):
        pos = (pos + steps) % len(lst)
        pos += 1
        lst.insert(pos, value)
        value += 1

    return lst, pos


# lst, pos = spinlock(steps=316, insertions=2017)
# print lst[pos + 1]

# ==== Part 2 ====

lst, _ = spinlock(steps=316, insertions=50000000)
print lst[lst.index(0) + 1]
