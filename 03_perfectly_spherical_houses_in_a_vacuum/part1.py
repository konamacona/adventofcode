# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:
# 	> delivers presents to 2 houses: one at the starting location, and one to the east.
# 	^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# 	^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

import sys

houses = { "0,0": True }

x = 0
y = 0

for char in sys.stdin.read():
	if char == '<': #left
		x -= 1
	elif char == '>': #right
		x += 1
	elif char == '^': #up
		y += 1
	else:			#down
		y -= 1
	houses[str(x) + "," + str(y)] = True

print len(houses)
