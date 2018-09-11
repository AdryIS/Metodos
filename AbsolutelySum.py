Take a list of integers (positive or negative or both) and return the sum of the absolute value of each element.

def get_abs_sum(lst):
	suma = 0;
	for i in range (len(lst)):
		suma+=abs(lst[i]);
	return suma
