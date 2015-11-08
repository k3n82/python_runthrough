from guessadvisor import GuessAdviser

if __name__ == '__main__':
	ga = GuessAdviser()
	while True:
		try:
			x = int(input("Guess a number: "))

			value = ga.guess(x)
			if value is GuessAdviser.CORRECT:
				print("You guessed right!")
				break
			if value is GuessAdviser.LOWER:
				print("Your guess was too high.")
			if value is GuessAdviser.HIGHER:
				print("Your guess was too low.")
		except ValueError:
			print("Please select provide an integer.")
