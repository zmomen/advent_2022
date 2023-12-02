import os
import string

def part1():
    with open(os.getcwd() + '/input/adventofcode.com_2022_day_3_input.txt', 'r') as file:
        strings = str(string.ascii_lowercase) + str(string.ascii_uppercase)
        sum_priorities = 0
        for line in file:
            inp = line.strip()

            arr1 = []
            mid = len(inp) // 2
            for i in range(0, mid):
                arr1.append(inp[i])

            for j in range(mid, len(inp)):
                if inp[j] in arr1:
                    sum_priorities += strings.index(inp[j]) + 1
                    break
        print("PART1", sum_priorities)  # part 1


def part2():
    with open(os.getcwd() + '/input/adventofcode.com_2022_day_3_input.txt', 'r') as file:
        strings = str(string.ascii_lowercase) + str(string.ascii_uppercase)
        groups_of_three_arr = []
        groups_of_three_counter = 0
        sum_priorities = 0
        for line in file:
            inp = line.strip()
            groups_of_three_counter += 1
            groups_of_three_arr.append(inp)
            if groups_of_three_counter < 3:
                continue
            else:
                arr1 = []
                groups_of_three_arr = sorted(groups_of_three_arr)

                for letter in groups_of_three_arr[0]:
                    arr1.append(letter)

                for ch in arr1:
                    if ch in groups_of_three_arr[1] and ch in groups_of_three_arr[2]:
                        sum_priorities += strings.index(ch) + 1
                        break

                groups_of_three_arr = []
                groups_of_three_counter = 0

        print("PART2", sum_priorities)  # part 2


part1()
part2()
