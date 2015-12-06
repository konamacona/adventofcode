# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:
# 	It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# 	It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# 	It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# For example:
# 	ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# 	aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# 	jchzalrnumimnmhp is naughty because it has no double letter.
# 	haegwjzuvuyypxyu is naughty because it contains the string xy.
# 	dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?
import sys

def double(s):
	last = ""
	for c in s:
		if c == last:
			return True
		last = c
	return False

def three_vowels(s):
	vowels = ['a','e','i','o','u']
	count = 0
	for v in vowels:
		count += s.count(v)
	return count >= 3

def no_pairs(s):
	badpairs = ['ab', 'cd', 'pq', 'xy']
	for p in badpairs:
		if p in s:
			return False
	return True

count = 0
for line in sys.stdin.readlines():
	if double(line) and three_vowels(line) and no_pairs(line):
		count += 1

print count