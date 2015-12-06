# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:
# 	turn on 0,0 through 999,999 would turn on (or leave on) every light.
# 	toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# 	turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

# After following the instructions, how many lights are lit?

import sys

SIZE = 1000

lights = [[False for x in range(SIZE)] for c in range(SIZE)]

def set_range(setting, x1, y1, x2, y2):
	for y in range(y1, y2 + 1):
		for x in range(x1, x2 + 1):
			if setting == 'Toggle':
				lights[y][x] = not lights[y][x]
			else:
				lights[y][x] = setting

def count_lights():
	count = 0
	for y in range(0, SIZE):
		for x in range(0, SIZE):
			if lights[y][x] == True:
				count += 1
	return count

def try_parse_int(s, base=10, val=None):
	try:
		return int(s, base)
	except ValueError:
		return val

for line in sys.stdin.readlines():
	line = line.replace(',', ' ')
	x1, y1, x2, y2 = filter(lambda x: x != None, map(try_parse_int, line.split()))
	setting = 'Toggle'
	if 'on' in line:
		setting = True
	elif 'off' in line:
		setting = False
	set_range(setting, x1, y1, x2, y2)

print str(count_lights())