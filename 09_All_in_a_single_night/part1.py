# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

# For example, given the following distances:
# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141

# The possible routes are therefore:\
# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982

# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

# What is the distance of the shortest route?



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

shortest = sys.maxsize
for p in permutations(list(nodes)):
	dist = 0
	for i in range(len(p) - 1):
		dist += adjList[p[i]][p[i+1]]
	shortest = min(shortest, dist)

print shortest