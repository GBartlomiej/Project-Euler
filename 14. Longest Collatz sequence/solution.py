def length_of_chain(start: int):
    number = start
    count = 1
    while number!=1:
        count += 1
        number = generate_next(number)
    return count

def generate_next(current: int):
    if current%2 == 0:
        return current/2
    else:
        return (current*3)+1

m = 0
M = 0
for number in range(999999, 1, -2):
    temp = length_of_chain(number)
    if m<temp:
        m = temp
        M = number
        print(f"{number=}, {temp}")