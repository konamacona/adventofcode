# The next year, just to show off, Santa decides to take the route with the longest distance instead.

# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

# What is the distance of the longest route?


#TSP: BFI fer dayz
import sys

nodes = set()
adjList = dict() #adjacency list

for line in sys.stdin.readlines():
	cities, dist = line.split(' = ')
	c1, c2 = cities.split(' to ')
	nodes.add(c1)
	nodes.add(c2)
	if c1 not in adjList.keys():
		adjList[c1] = dict()
	adjList[c1][c2] = int(dist)
	if c2 not in adjList.keys():
		adjList[c2] = dict()
	adjList[c2][c1] = int(dist)

#returns the list of permutations of the set
def permutations(set):
	if len(set) <= 1:
		yield set
	else:
		for subset in permutations(set[1:]):
			for i in range(len(set)):
				yield subset[:i] + set[0:1] + subset[i:]

longest = 0
for p in permutations(list(nodes)):
	dist = 0
	for i in range(len(p) - 1):
		dist += adjList[p[i]][p[i+1]]
	longest = max(longest, dist)

print longest