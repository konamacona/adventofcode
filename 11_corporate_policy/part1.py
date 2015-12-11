# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:
# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

# For example:
# hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
# abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# abbcegjk fails the third requirement, because it only has one double letter (bb).
# The next password after abcdefgh is abcdffaa.
# The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

# Given Santa's current password (your puzzle input), what should his next password be?

# --- Part Two ---

# Santa's password expired again. What's the next one?

import sys
import string

alphabet = string.ascii_lowercase

def increment(p):
	p = list(p)
	for i in reversed(range(len(p))):
		index = alphabet.index(p[i])
		index += 1
		if index == 26:
			index = 0
		p[i] = alphabet[index]
		if index != 0:
			break
	return ''.join(p)

def inc_straight(p):
	for i in range(len(p) - 2):
		if p[i:i+3] in alphabet:
			return True
	return False

def pairs(p):
	pairs = 0
	skip = 0
	for i in range(len(p) - 1):
		if skip > 0:
			skip -= 1
			continue
		l1, l2 = p[i:i+2]
		if l1 == l2:
			pairs += 1
			skip += 1
	return pairs >= 2

def no_bad(p):
	return 'i' not in p and 'o' not in p and 'l' not in p

def is_valid(p):
	return no_bad(p) and pairs(p) and inc_straight(p)

def generate_next(p):
	while True:
		p = increment(p)
		if (is_valid(p)):
			return p

password = "hepxcrrq"

password = generate_next(password)
print('part1: ' + password)
password = generate_next(password)
print('part1: ' + password)