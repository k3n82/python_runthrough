import string
import random

def generate_name(min_length = 4, max_length=10):
	""" Returns a random string with atmost two vowels seperating each constanant and following every two vowels, there must be a constanant """

	alphabets = list(string.ascii_lowercase)

	vowels = ['a','e','i','o','u','y']
	constants = [i for i in alphabets if i not in vowels]

	length = random.randint(min_length, max_length)

	name = []

	vowel_time = 0
	vowel_start = random.randint(0,1) == 1
	vowel_turn = False

	for i in range(0,length):
		if (vowel_start and i == 0) or (vowel_time <= 1) or vowel_turn:
			name.append(random.choice(vowels))
			vowel_time += 1
			vowel_turn = False
			continue
		name.append(random.choice(constants))
		vowel_turn = True

	return ''.join(name)

