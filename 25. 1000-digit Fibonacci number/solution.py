n1 = 1
n2 = 1
idx = 1
while len(str(n2))<1000:
    temp = n1
    n1 = n1+n2
    n2 = temp
    idx += 1

print(idx)