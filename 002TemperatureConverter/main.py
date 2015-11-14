from tempconv import *
import argparse

f = 'fahrenheit'
c = 'celsius'
k = 'kelvin'

TempArgs = {
	f: {'short': '-f', 'long': '--fahrenheit'},
	c: {'short': '-c', 'long': '--celsius'},
	k: {'short': '-k', 'long': '--kelvin'}
}

parser = argparse.ArgumentParser(description='Converts temperature between fahrenheit, celsius, and kelvin')

for name, temp in TempArgs.items():
	parser.add_argument(temp['short'], temp['long'], help=name.title(), metavar=name.title(), nargs='*', type=float, dest=name)

args = parser.parse_args()

frm = {name: getattr(args, name) for name, temp in TempArgs.items() if getattr(args, name) }
dst = [i for i in TempArgs.keys() if getattr(args, i) is not None and len(getattr(args, i)) == 0]

conversion = {(f,c):ftc, (f,k):ftk, (c,f):ctf, (c,k):ctk, (k,c):ktc, (k,f):ktf}
result = {i: {j:[conversion[(i,j)](a) for a in v] for j in dst} for i, v in frm.items()}

for i, v in result.items():
	[[print(i.capitalize() + ': '), print(*[str(x) + j[:1].upper() for x in k])] for j, k in v.items()]

