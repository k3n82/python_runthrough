def ctk(celsius):
	return celsius + 273.15

def ctf(celsius):
	return (celsius * 1.8) + 32

def ftc(fahrenheit):
	return (fahrenheit - 32) / 1.8

def ftk(fahrenheit):
	return ctk(ftc(fahrenheit))

def ktc(kelvin):
	return kelvin - 273.15

def ktf(kelvin):
	return ctf(ktc(kelvin))
