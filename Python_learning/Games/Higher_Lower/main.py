import random
from game_data import data


def pick_random():
    pick = random.choice(data)
    list_of_values = list(pick.values())
    # print(*list_of_values, sep="a ")
    # for i in range(0,len(list_of_values)):
    # 	print(list_of_values[i])

    texts = [" ", " ", ", a ", ", from "]
    # for texts, items in zip(texts, list_of_values):
    # 	print(texts + str(items), end=" ")
    for index, item in enumerate(list_of_values):
        if index + 1 in [1, 3, 4]:
            print(texts[index] + str(item), end=" ")
    return list_of_values


print("\nCompare A: ")
player_A = pick_random()
no_of_followers_A = player_A[1]
score = 0

play = True
while play == True:

    print("\n\nAgainst B: ")
    player_B = pick_random()
    no_of_followers_B = player_B[1]
    user_choice = (input("\n\nWho are having the most followers A or B ?  ")).lower()

    if user_choice == "a":
        if no_of_followers_A > no_of_followers_B:
            print(f"A is having {no_of_followers_A} more than followers {no_of_followers_B}")
            winner = player_A
            score += 1
            print(f"You Won ! and score is {score}")
        else:
            print(f"B is having  {no_of_followers_B} more followers than A  {no_of_followers_A}")
            winner = player_B
            print(f"Oh you Loose and score is {score}")
    if user_choice == "b":
        if no_of_followers_B > no_of_followers_A:
            print(f"B is having  {no_of_followers_B} more followers than A {no_of_followers_A}")
            winner = player_B
            score += 1
            print(f"You Won ! and score is {score}")
        else:
            print(f"A is having  {no_of_followers_A} more followers than B  {no_of_followers_B}")
            winner = player_A
            print(f"Oh you Loose and score is {score}")

    continue_playing = input("Do you want to continue playing? Y/N  :  ")
    if continue_playing == "n":
        exit(0)
    else:
        print("\nCompare A: ")
        texts = [" ", " ", ", a ", ", from "]
        for index, item in enumerate(winner):
            if index + 1 in [1, 3, 4]:
                print(texts[index] + str(item), end=" ")
