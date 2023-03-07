from itertools import permutations


class Player:
	def __init__(self, name, catcher_skill, pitching_skill, infield_skill, outfield_skill, throwing_skill, catching_skill):
		self.name = name
		self.catcher_skill = catcher_skill
		self.pitching_skill = pitching_skill
		self.infield_skill = infield_skill
		self.outfield_skill = outfield_skill
		self.throwing_skill = throwing_skill
		self.catching_skill = catching_skill
	
	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name		


def score_order(order, players):
	score = 0
	#print(order)
	for idx, player in enumerate(players):
		if order[idx] == 'P':
			score = score + players[idx].pitching_skill*4
			#print(players[idx].name)
		if order[idx] == 'C':
			score = score + players[idx].catcher_skill*3
		if (order[idx] == '1B' or order[idx] == '2B' or order[idx] == '3B' or order[idx] == 'SS'):
			score = score + players[idx].infield_skill
			if(order[idx] == '1B'):
				score = score + players[idx].catching_skill
			if(order[idx] == '3B'):
				score = score + players[idx].throwing_skill
			if(order[idx] == '2B' or order[idx] == 'SS'):
				score = score + players[idx].infield_skill
		if (order[idx] == 'LF' or order[idx] == 'RF' or order[idx] == 'CF'):
			score = score + players[idx].outfield_skill
	return score



players = []
players.append(Player('Ethan', 5, 4, 3, 4, 3, 4))
players.append(Player('Eitan', 3, 3, 3, 3, 4, 3))
players.append(Player('Dalton', 2, 4, 4, 4, 4, 4))
players.append(Player('Sam', 2, 5, 5, 5, 5, 5))
players.append(Player('Lochlan', 2, 3, 4, 4, 5, 4))
players.append(Player('Hudson', 2, 1, 2, 3, 2, 3))
players.append(Player('Logan', 3, 2, 2, 3, 3, 3))
players.append(Player('Albert', 2, 2, 2, 2, 3, 2))
players.append(Player('Vidyuth', 1, 1, 3, 2, 2, 3))
players.append(Player('Shriyan', 1, 1, 2, 2, 2, 2))
players.append(Player('Niles', 1, 4, 4, 4, 4, 4))

print(players)

l = list(permutations(['P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', '-', '-']))
scores = []

#print(l[0:20])

for idx, lineup in enumerate(l):
	scores.append(score_order(l[idx], players))

max_value = max(scores)
index = scores.index(max_value)
print(l[index])
print(str(players))
