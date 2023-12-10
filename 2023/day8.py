from utils import read_into_list


def solve(input_arr, part):
    moving_pattern = list(input_arr[0])
    if part == 1:
        mapper = {}
        for i in range(2, len(input_arr)):
            splitter = input_arr[i].split("=")
            key = splitter[0].strip()
            values = [splitter[1].split(",")[0].strip(
            )[1:], splitter[1].split(",")[1][:-1].strip()]
            mapper[key] = values

        cur_key = 'AAA'
        steps = 0
        i = 0
        while True:
            direction = moving_pattern[i % len(moving_pattern)]
            i += 1
            if direction == 'R':
                cur_key = mapper[cur_key][1]
            else:
                cur_key = mapper[cur_key][0]

            if cur_key == 'ZZZ':
                return steps+1
            else:
                steps += 1
    else: # part 2. infinite loop :/ 
        mapper = {}
        start_paths = []
        for i in range(2, len(input_arr)):
            splitter = input_arr[i].split("=")
            key = splitter[0].strip()
            if key[-1] == 'A':
                start_paths.append(key)
            values = [splitter[1].split(",")[0].strip()[1:],
                      splitter[1].split(",")[1][:-1].strip()]
            mapper[key] = values
        # print(mapper)
        print(start_paths)
        steps = 0
        i = 0
        while True:
            direction = moving_pattern[i % len(moving_pattern)]
            for kk in range(len(start_paths)):
                if direction == 'R':
                    start_paths[kk] = mapper[start_paths[kk]][1]
                else:
                    start_paths[kk] = mapper[start_paths[kk]][0]

            if all([x[-1] == 'Z' for x in start_paths]):
                return steps+1
            else:
                steps += 1
            i += 1


if __name__ == '__main__':
    part1_test_case = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".split('\n')

    # print(solve(part1_test_case, 1))
    text_arr = read_into_list('in_d8.txt')
    # print(solve(text_arr, 1))
    print(solve(text_arr, 2))
