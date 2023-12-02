import os

with open(os.getcwd() + '/input/adventofcode.com_2022_day_2_input.txt', 'r') as file:
    total_score = 0
    adjusted_score = 0
    hash = {
        'X': 1,
        'Y': 2,
        'Z': 3,
        'AX': 3,
        'AY': 6,
        'AZ': 0,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 6,
        'CY': 0,
        'CZ': 3,
    }

    hash = {
        'X': 1,
        'Y': 2,
        'Z': 3,
        'AX': 3,
        'AY': 6,
        'AZ': 0,
        'BX': 0,
        'BY': 3,
        'BZ': 6,
        'CX': 6,
        'CY': 0,
        'CZ': 3,
    }

    hash2 = {
        'X': 0,
        'Y': 3,
        'Z': 6,
        'AX': 3,
        'BX': 1,
        'CX': 2,
        'AY': 1,
        'BY': 2,
        'CY': 3,
        'AZ': 2,
        'BZ': 3,
        'CZ': 1,
    }

    for line in file:
        # read line, split it in two values, 
        # then join them so it creates a string key to be looked up in the hash dict. 
        outcome = "".join(line.strip().split(' '))
        total_score += hash[outcome] + hash[outcome[-1]]
        adjusted_score += hash2[outcome] + hash2[outcome[-1]]
    print(total_score)  # part 1
    print(adjusted_score)  # part 2
