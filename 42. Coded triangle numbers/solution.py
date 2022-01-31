import os

def get_word_value(word):
    value = 0
    for letter in word:
        value += ord(letter)-64
    return value

def get_triangle_numbers(n):
    triangles = []
    for number in range(1,n):
        triangles.append(int(number*(number+1)/2))
    return triangles 

words = []
path = os.path.dirname(os.path.abspath(__file__))
with open(path+"\\words.txt") as f:
    for line in f:
        words= line.split(',')

words = [word[1:-1] for word in words]
numbers = set(get_triangle_numbers(100))
how_many_triangle_words = 0
for word in words:
    if get_word_value(word) in numbers:
        how_many_triangle_words+=1
print(how_many_triangle_words)