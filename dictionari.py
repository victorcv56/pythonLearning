#makes a list and fills it with 100 random numbers
import random as r

li = []

def fill_list(li):
    count = 0
    while count < 100:
        li.append(r.randint(1,101))
        count += 1


def see_list(li):
    for n in li:
        print(n)

#shows even numbers in list
def see_evens(li):
    for n in li:
        if n % 2 == 0:
            print(n)

