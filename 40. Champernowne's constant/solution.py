def generete_string(n):
    return "0."+''.join([str(i) for i in range(1, n)])


number = generete_string(1000000)
multip = 1
for n in range(7):
    multip *= int(number[1+10**n])

print(multip)