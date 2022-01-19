import os


names = []
path = os.path.dirname(os.path.abspath(__file__))

with open(path+"\\names.txt") as f:
    for line in f:
        names = sorted(line.lower().replace("\"", "").split(","))

s = 0
for idx, name in enumerate(names):
    s += sum((ord(letter) - 96) for letter in name)*(idx+1)

print(s)
