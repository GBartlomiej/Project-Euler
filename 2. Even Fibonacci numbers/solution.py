x1 = 1
x2 = 2
sum = 0
while x2<4000000:
    if x2%2==0:
        sum += x2
    temp = x2
    x2 = x1+x2
    x1 = temp
print(sum)
