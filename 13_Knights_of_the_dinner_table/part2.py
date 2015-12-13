
import sys

people = dict()

for line in sys.stdin.readlines():
	s = line.split()
	if s[0] not in people.keys():
		people[s[0]] = dict()
	i = int(s[3])
	if s[2] == 'lose':
		i *= -1
	people[s[0]][s[10].replace('.', '')] = i

me = dict()
for p in people.keys():
	me[p] = 0
	people[p]['me'] = 0

people['me'] = me

def calc_cost(p):
	res = 0
	for i in range(len(p)):
		k = i - 1
		j = i + 1
		if i == 0:
			k = len(p) - 1
		if i == len(p) - 1:
			j = 0
		res += people[p[i]][p[j]] + people[p[i]][p[k]]
	return res

#returns the list of permutations of the set
def permutations(set):
	if len(set) <= 1:
		yield set
	else:
		for subset in permutations(set[1:]):
			for i in range(len(set)):
				yield subset[:i] + set[0:1] + subset[i:]

print(max(map(calc_cost, permutations(list(people.keys())))))