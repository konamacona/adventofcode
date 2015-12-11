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