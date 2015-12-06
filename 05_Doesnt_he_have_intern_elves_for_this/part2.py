# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:
# 	It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# 	It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# For example:
# 	qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# 	xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# 	uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# 	ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

# How many strings are nice under these new rules?

import sys

def two_pairs(s):
	pairs = []
	for n in range(0, len(s) - 1):
		pairs.append(s[n:n+2])

	for i in range(0, len(pairs)):
		#only worry about indices after the pair
		if pairs[i] in pairs[i + 2:len(pairs)]:
			return True

	return False

def sandwich(s):
	for i in range(0, len(s)):
		if i + 2 < len(s) and s[i] == s[i + 2]:
			return True
	return False

count = 0
for line in sys.stdin.readlines():
	if two_pairs(line) and sandwich(line):
		count += 1

print count