import os 

with open(os.getcwd() + '/input/adventofcode.com_2022_day_1_input.txt', 'r') as file:
    ll = []
    ll.append(0)
    for line in file:
        if line == '\n':
            ll.append(0)
        else:
            ll[-1] += int(line.strip())
    print(max(ll)) # part 1
    print(sum(sorted(ll)[-3:])) # part 2 

