import random


def random_cards():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	#card = random.choice(cards)
	card = random.sample((cards), 2)
	return card


user=[]
computer=[]
user.append(random_cards())
computer.append(random_cards())

sum_user = sum(user)
sum_computer = sum(computer)
print(f"Your cards {user} adds to {sum_user}")
print(f"Computer cards {computer} adds to  {sum_computer}")


ace = 11
if sum_user >=21 and ace in user:
	print("You Won !")
	exit(0)
if sum_computer >=21 and ace in computer:
	print("You Lost !")

if sum_user >=21:
	if ace in user:
		ace = 1
		sum_user +=ace
		if sum_user >=21:
			print("You Lost by making ace as 1 !")
	else:
		print("You Lost !")
else:
	another_card = input("Do You want to draw another card y/n: ")
	if another_card =='y':
		random_cards()