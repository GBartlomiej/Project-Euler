size = 1001
number_on_diagonal = 1
summation = number_on_diagonal
for i in range(2,size,2):
    for j in range(4):
        number_on_diagonal += i
        summation += number_on_diagonal

print(summation)
