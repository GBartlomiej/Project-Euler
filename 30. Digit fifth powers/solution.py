def find_numbers(n):
    return [i for i in range(2, n) if check_if_digit_power(i)]

def check_if_digit_power(n):
    string = str(n)
    return sum([*map(lambda x: int(x)**5, string)])==n

how_many_to_check=1_000_000
numbers = find_numbers(how_many_to_check)
print(numbers)
print(sum(numbers))
