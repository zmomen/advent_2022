from utils import read_into_list


def solve(part):
    lines = read_into_list('in_d1.txt')
    totaler = 0
    for line in lines:
        if part == 2:
            line = line.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e")\
                .replace("four", "f4r").replace("five", "f5e").replace("six", "s6x")\
                .replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
        potential_num = ""
        for i in range(len(line)):
            if str.isdigit(line[i]):
                potential_num += line[i]
                break

        for j in range(len(line)-1, -1, -1):
            if str.isdigit(line[j]):
                potential_num += line[j]
                break
        totaler += int(potential_num)
    return totaler


print("part1:", solve(1))
print("part2:", solve(2))
