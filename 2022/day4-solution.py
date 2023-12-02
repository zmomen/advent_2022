import os

def func():
    with open(os.getcwd() + '/input/adventofcode.com_2022_day_4_input.txt', 'r') as file:
        dups = 0
        dups2 = 0
        for line in file:
            ranges = [b for b in [
                y.split('-') for y in [x for x in line.strip().split(',')]]]
            ranges = [int(num) for rang in ranges for num in rang]
            # print(ranges)

            if (ranges[0] in range(ranges[2], ranges[3]+1)
                and ranges[1] in range(ranges[2], ranges[3]+1)) \
                or (ranges[2] in range(ranges[0], ranges[1]+1)
                    and ranges[3] in range(ranges[0], ranges[1]+1)):
                dups += 1
            if (ranges[0] in range(ranges[2], ranges[3]+1)
                or ranges[1] in range(ranges[2], ranges[3]+1)) \
                or (ranges[2] in range(ranges[0], ranges[1]+1)
                    or ranges[3] in range(ranges[0], ranges[1]+1)):
                dups2 += 1
        print(dups)
        print(dups2)


func()
