# http://adventofcode.com/2017/day/4

# ==== Part 1 ====

# example = """aa bb cc dd ee
# aa bb cc dd aa
# aa bb cc dd aaa"""


def count_valid_passphrases(passphrases):
    count = 0
    for passphrase in passphrases.splitlines():
        words = []
        valid = True
        for word in passphrase.split():
            if word in words:
                # Found a duplicate
                valid = False
                break
            else:
                words.append(word)

        if valid:
            count += 1

    return count


# print count_valid_passphrases(input)

# ==== Part 2 ====

# example = """abcde fghij
# abcde xyz ecdab
# a ab abc abd abf abj
# iiii oiii ooii oooi oooo
# oiii ioii iioi iiio"""


def count_valid_passphrases_2(passphrases):
    count = 0
    for passphrase in passphrases.splitlines():
        sorted_words = []
        valid = True
        for word in passphrase.split():
            # Sort the word by its characters
            sorted_word = ''.join(sorted(word))
            if sorted_word in sorted_words:
                # Found an anagram
                valid = False
                break
            else:
                sorted_words.append(sorted_word)

        if valid:
            count += 1

    return count


input = open('day4.txt').read()
print count_valid_passphrases_2(input)