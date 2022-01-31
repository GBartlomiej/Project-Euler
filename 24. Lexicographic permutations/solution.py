from itertools import permutations

for idx, number in enumerate(permutations(range(10), 10)):
    if idx+1 == 1_000_000:
        print(''.join([*map(str, number)]))
        break