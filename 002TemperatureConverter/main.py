import tempconv
import argparse

TempArgs = {
	'fahrenheit': {'short': '-f', 'long': '--fahrenheit'},
	'celsius'	: {'short': '-c', 'long': '--celsius'},
	'kelvin'	: {'short': '-k', 'long': '--kelvin'}
}

parser = argparse.ArgumentParser(description='Converts temperature between fahrenheit, celsius, and kelvin')

for name, temp in TempArgs.items():
	parser.add_argument(temp['short'], temp['long'], help=name.title(), metavar=name.title(), nargs='*', type=float, dest=name)

args = parser.parse_args()

convertees = {name: getattr(args, name) for name, temp in TempArgs.items() if getattr(args, name) }
converter = {name: {} for name, temp in TempArgs.items() if getattr(args, name) is not None and len(getattr(args, name)) == 0 }

for conv_temp, container in converter.items():
	if conv_temp is 'fahrenheit':
		"""  Converts Temperatures to Fahrenheit """
		for name, values in convertees.items():
			if name == 'celsius':
				container['celsius'] = [tempconv.celsius_to_fahrenheit(v) for v in values ]
			if name == 'kelvin':
				container['kelvin'] = [tempconv.kelvin_to_fahrenheit(v) for v in values ]

	elif conv_temp is 'celsius':
		"""  Converts Temperatures to Celsius """
		for name, values in convertees.items():
			if name == 'fahrenheit':
				container['fahrenheit'] = [tempconv.fahrenheit_to_celsius(v) for v in values ]
			if name == 'kelvin':
				container['kelvin'] = [tempconv.kelvin_to_celsius(v) for v in values ]

	elif conv_temp is 'kelvin':
		"""  Converts Temperatures to Kelvin """
		for name, values in convertees.items():
			if name == 'celsius':
				container['celsius'] = [tempconv.celsius_to_kelvin(v) for v in values ]
			if name == 'fahrenheit':
				container['fahrenheit'] = [tempconv.fahrenheit_to_kelvin(v) for v in values ]

def fod(dict):
	""" short for first_of_dictionary """
	return next(iter(dict.values()))


def simple_print(array):
	print(*array, sep=' ')

for i, v in converter.items():
	simple_print(fod(v))
