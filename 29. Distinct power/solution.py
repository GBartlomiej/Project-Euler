def len_distinct_power(a, b):
    A = range(2, a+1)
    B = range(2, b+1)
    return len(list(set([element for sublist in [*map(lambda x: [x**b for b in B],A)] for element in sublist])))

print(len_distinct_power(100,100))