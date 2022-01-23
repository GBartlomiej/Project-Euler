#in this problem we have combinations of set that contains the same amount of down/right movement
#that means in 2x2 grid we have 6 combinations each containing 2 down, 2 right movement.
#In math it's called Central binomial coefficient and more info can be found here:
# https://en.wikipedia.org/wiki/Central_binomial_coefficient
#So to calculate 20th element we use formula for that coefficient
from math import factorial
nth = 20
coeff = int(factorial(2*nth)/factorial(nth)**2)
print(coeff)