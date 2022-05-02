from Words import list_of_words
from ASCI_img import ASCI
import random
game_is_on = True
lives = 6
import time

random_word = random.choice(list_of_words)
random_list = []

for letter in random_word:
	random_list.append("_")
print("Welcome To Hang-Man")
time.sleep(2)
print("Theres one inconvenience with the program")
time.sleep(2)
print("Once you guessed the whole word in the console and the winner text doesnt pop up")
time.sleep(2)
print("Press Enter :)")
time.sleep(2)
print("Sorry for the inconvenience ")
time.sleep(2)
print("Lets proceed shall we ?")

while game_is_on:

	container = ""
	for letter in random_list:
		container += letter

	# print(f"{random_word} : is the word smile")
	print(random_list)
	my_guess = input("Guess a letter :)\n")


	if random_word in container:
		game_is_on = False
		print(f"You win ! Congratulations the word was {random_word} ")

	elif my_guess not in random_word:
		lives -= 1
		if lives == 0:
			print(f"You have {lives} lives remaining YOU LOSE !")
			game_is_on = False
			print(f"The word was {random_word}")

	if my_guess in container:
		print("You guessed that letter already ! :)")

	for position in range(len(random_word)):
		letters = random_word[position]
		if letters == my_guess:
			random_list[position] = letters

	if lives == 6:
		print(ASCI[6])
	elif lives == 5:
		print(ASCI[5])
	elif lives == 4:
		print(ASCI[4])
	elif lives == 3:
		print(ASCI[3])
	elif lives == 2:
		print(ASCI[2])
	elif lives == 1:
		print(ASCI[1])
	elif lives == 0:
		print(ASCI[0])
