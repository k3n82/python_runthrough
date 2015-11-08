import namegen
import sys

if __name__ == '__main__':
	if len(sys.argv) == 1:
		print(namegen.generate_name())
	elif len(sys.argv) == 2:
		print(namegen.generate_name(int(sys.argv[1])))
	elif len(sys.argv) == 3:
		print(namegen.generate_name(int(sys.argv[1]), int(sys.argv[2])))