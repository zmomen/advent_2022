import os


def func(marker):
    with open(os.getcwd() + '/2022/input/adventofcode.com_2022_day_6_input.txt', 'r') as file:
        res = file.read().strip()
        seeker = 0
        while seeker+marker < len(res):
            cur = set(res[seeker:seeker+marker])
            if len(cur) == marker:
                print(res[seeker:seeker+marker], cur, seeker+marker)
                break
            seeker+=1



func(4) # part 1
func(14) # part 2 
