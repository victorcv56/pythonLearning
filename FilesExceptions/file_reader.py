filename = 'Pi/Pi1MDP.txt'

with open(filename) as pi:
    lines = pi.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(f"{pi_string}")
print("There are %d digits in pi" % len(pi_string))