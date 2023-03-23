import random as r
li = []
count = 0

while count < 100:
    li.append(r.randint(1, 20))
    count += 1

print(li)