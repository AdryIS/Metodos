Create a function that takes a list of numbers and returns a list where each number is the sum of itself + all previous numbers in the list.

def cumulative_sum(lst):
    lista = []
    for i in range(len(lst)):
        if i>0:
            lista.append(lista[-1]+ lst[i])
        else:
            lista.append(lst[i])
    return lista
