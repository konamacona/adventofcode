# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:
# 	turn on 0,0 through 0,0 would increase the total brightness by 1.
# 	toggle 0,0 through 999,999 would increase the total brightness by 2000000

import sys

SIZE = 1000

lights = [[0 for x in range(SIZE)] for c in range(SIZE)]

def set_range(change, x1, y1, x2, y2):
	for y in range(y1, y2 + 1):
		for x in range(x1, x2 + 1):
			lights[y][x] += change
			if lights[y][x] < 0:
				lights[y][x] = 0

def count_lights():
	count = 0
	for y in range(0, SIZE):
		for x in range(0, SIZE):
			count += lights[y][x]

	return count

def try_parse_int(s, base=10, val=None):
	try:
		return int(s, base)
	except ValueError:
		return val

print str(count_lights())

for line in sys.stdin.readlines():
	line = line.replace(',', ' ')
	x1, y1, x2, y2 = filter(lambda x: x != None, map(try_parse_int, line.split()))
	if 'on' in line:
		setting = 1
	elif 'off' in line:
		setting = -1
	else:
		setting = 2
	set_range(setting, x1, y1, x2, y2)

print str(count_lights())