# Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

# For example:

# ) causes him to enter the basement at character position 1.
# ()()) causes him to enter the basement at character position 5.
# What is the position of the character that causes Santa to first enter the basement?

import sys

floor = 0
char_count = 1 # 1 as per problem

for char in sys.stdin.read():
	if char == "(":
		floor += 1
	else:
		floor -= 1
	if floor == -1:
		break
	char_count += 1


print char_count