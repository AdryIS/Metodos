Create a function that takes a list of numbers and returns the following statistics:
Minimum Value
Maximum Value
Sequence Length
Average Value


def minMaxLengthAverage(lst):
	a = min(lst);
	b = max(lst);
	c = len(lst);
	d = (sum(lst))/c
	lista = [];
	lista.append(a);
	lista.append(b);
	lista.append(c);
	lista.append(d);
	return lista;
	
