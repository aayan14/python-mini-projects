import random
class Roles:
	def __init__(self,role,defeaters,opponent):
		self.role = role
		self.defeaters = defeaters
		self.opponent = opponent

	def result(self):
		if self.opponent in self.defeaters:
			return -1
		elif self.opponent == self.role:
			return 0
		else:
			return 1
	pass



def printHeader(rolesAvailable, rolesCanDefeat):
	print('*****WELCOME TO 15 WAY ROCK PAPER SCISSOR*****')
	print()
	wantRules = input('Do you want to know the rules of the game?(Y/N)')
	if wantRules == 'Y':
		for i in rolesCanDefeat.keys():
			print(i + ' can defeat')
			print(rolesCanDefeat[i])
	else:
		pass
	print()
	print()
	print('Roles Available:\n')
	print(rolesAvailable)


def gamePlay(rolesCanDefeat):
	
	playerName1 = input("Player Name")
	print(playerName1 + " v/s Computer")
	compPoints = 0
	player1Points = 0
	while compPoints < 5 and player1Points < 5:
		role = input("Select A Role (select a role from roles available)")
		if role not in rolesCanDefeat.keys():
			print('Please Select A Role From Roles Available  ')
			role = input("Select A Role (select a role from roles available)") 
		opponent = random.choice(rolesAvailable)
		defeaters = rolesCanDefeat[role]
		player1 = Roles(role,defeaters,opponent)
		res = player1.result()
		if res == -1:
			compPoints += 1
			print('Computer: ' + opponent)
			print('Computer Wins The Round!!')
		elif res == 0:
			print('Computer: ' + opponent)
			print('Its A Draw!!')
		else:
			player1Points += 1
			print('Computer: ' + opponent)
			print(playerName1 + ' Wins The Round!!')
		print('Points:\n')
		print(playerName1 + ':')
		print(player1Points)
		print('Computer: ')
		print(compPoints)
	
	if compPoints > player1Points:
		print('Computer Wins The Game!!')
	else:
		print(playerName1 + ' Wins The Game!!')


rolesAvailable = 'Rock Gun Lightning Devil Dragon Water Air	Paper Sponge Wolf Tree Human Snake Scissors Fire'.split()
rolesCanDefeat = {
	'Rock':'Gun Lightning Devil Dragon Water Air Paper'.split(),
	'Gun':'Lightning Devil Dragon Water Air Paper Sponge'.split(),
	'Lightning':'Devil Dragon Water Air Paper Sponge Wolf'.split(),
	'Devil':'Dragon Water Air Paper Sponge Wolf Tree'.split(),
	'Dragon':'Water Air Paper Sponge Wolf Tree Human'.split(),
	'Water':'Air Paper Sponge Wolf Tree Human Snake'.split(),
	'Air':'Paper Sponge Wolf Tree Human Snake Scissors'.split(),
	'Paper':'Sponge Wolf Tree Human Snake Scissors Fire'.split(),
	'Sponge':'Wolf Tree Human Snake Scissors Fire Rock'.split(),
	'Wolf':'Tree Human Snake Scissors Fire Rock Gun'.split(),
	'Tree':'Human Snake Scissors Fire Rock Gun Lightning'.split(),
	'Human':'Snake Scissors Fire Rock Gun Lightning Devil'.split(),
	'Snake':'Scissors Fire Rock Gun Lightning Devil Dragon'.split(),
	'Scissors':'Fire Rock Gun Lightning Devil Dragon Water'.split(),
	'Fire':'Rock Gun Lightning Devil Dragon Water Air'.split(),
}
printHeader(rolesAvailable,rolesCanDefeat)
gamePlay(rolesCanDefeat)

	