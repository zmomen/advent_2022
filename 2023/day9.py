from utils import read_into_list


def solve(input_arr, part):

    # part1
    # read each array. start, subtract and replace the previous.
    # each iter stop a position prior
    # end iter when all zeros or the position prior is 1.
    # then total the result. per line. accumulate.

    readings = []
    for line in input_arr:
        readings.append(list(map(int, line.strip().split(" "))))

    accum = 0
    if part == 1:
        for reader in readings:
            size = len(reader)
            while size > 0:
                for i in range(1, size):
                    reader[i-1] = reader[i] - reader[i-1]
                if reader[-1] == 0:
                    break
                size -= 1
            accum = accum + sum(reader)
    
    else:
        for reader in readings:
            all1 = [reader]
            while not (len(set(all1[-1])) == 1 and all1[-1][0] == 0):
                interim = []
                for j in range(1, len(all1[-1])):
                    interim.append(all1[-1][j] - all1[-1][j-1])
                all1.append(interim)
            mid_val = all1[len(all1)-2][0]
            new_len = len(all1)-3
            while new_len > -1:
                mid_val = all1[new_len][0] - mid_val
                new_len-=1
            accum+= mid_val

    return accum


if __name__ == '__main__':
    text_arr = read_into_list('in_d9.txt')
    print(solve(text_arr, 1))
    print(solve(text_arr, 2))
