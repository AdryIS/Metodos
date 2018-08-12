Create a function that takes a string and returns the number (count) of vowels contained within it.


def count_vowels(txt):
	cont = 0
	vocales = ["a", "e", "i", "o", "u"]
	for x in range(len(txt)):
		if txt[x] in vocales:
			cont += 1
	return cont
