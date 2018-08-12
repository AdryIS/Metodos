Create a function that takes a list of numbers and returns the mean value.


def mean(lst):
	sumaLista = sum(lst)
	numero = len(lst)
	mean = sumaLista/numero
	return round(mean,2)
	
