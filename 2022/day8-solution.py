
def func():
    with open('/Users/zaidal-momen/Downloads/job hunt 2023q3/leetcode_python/advent_2022/input/' +
              'adventofcode.com_2022_day_8_input.txt', 'r') as file:
        counter = 0
        matrix = []
        for line in file:
            cols = 0
            line = line.strip()
            matrix.append([])
            for ch in line:
                matrix[counter].append(int(ch))
            counter+=1 


        # down
        m = n = 1
        while m < counter-1:
            matrix[m][n]



func()  # part 2
