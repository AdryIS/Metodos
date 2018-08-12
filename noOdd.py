Create a function that takes a list of numbers and returns only the even values.


def noOdds(lst):
	even = []
	for x in lst:
		if x % 2 == 0:
			even.append(x)
	return(even)
