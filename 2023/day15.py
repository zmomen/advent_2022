import copy

from utils import read_into_list


def hasher(word):
    cur = 0
    for ch in word:
        cur += ord(ch)
        cur *= 17
        cur %= 256
    return cur


def solve(input_arr, part):
    splitter = input_arr[0].split(',')
    if part == 1:
        accum = 0
        for word in splitter:
            accum += hasher(word)
        return accum

    else:
        # dictionary of numbers as keys.
        # each value is a dictionary with lens and focal strength.
        boxes = {}
        for word in splitter:
            operation = '-' if word[-1] == '-' else '='
            lens = ''
            focal_strength = 0
            if '-' in word:
                lens = word.split('-')[0]
            else:
                lens = word.split('=')[0]
                focal_strength = int(word.split('=')[1])

            box_num = int(hasher(lens))

            if box_num in boxes:
                if operation == '=':
                    boxes[box_num][lens] = focal_strength
                else:
                    if lens in boxes[box_num]:
                        del boxes[box_num][lens]
            else:
                if operation == '=':
                    boxes[box_num] = {lens: focal_strength}

    accum = 0
    for k, v in boxes.items():
        subc = 1
        for _, subv in v.items():
            # print('box_num', k+1, 'slot', subc, 'focal', subv)
            accum = accum + ((k+1) * subc * subv)
            subc += 1
    return accum


if __name__ == '__main__':
    text_arr = read_into_list('in_d15.txt')
    print(solve(text_arr, 1))
    print(solve(text_arr, 2))
