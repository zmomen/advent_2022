import copy

from utils import read_into_list


def transpose(matrix):
    return [[matrix[j][i]
             for j in range(len(matrix))] for i in range(len(matrix[0]))]


def swap(row, direction):
    swap_pos = 0
    if direction == 1:
        swap_pos = len(row)-1

        while row[swap_pos] in ['O', '#']:
            swap_pos -= 1

        for x in range(swap_pos, -1, -1):
            if row[x] == 'O':
                if swap_pos == x:
                    swap_pos -= 1
                    continue
                else:
                    row[swap_pos] = 'O'
                    row[x] = '.'
                    swap_pos -= 1
            elif row[x] == '.':
                continue
            else:
                swap_pos = x-1

    else:  # direction == 0
        while row[swap_pos] in ['O', '#']:
            swap_pos += 1

        for x in range(swap_pos, len(row)):
            if row[x] == 'O':
                if swap_pos == x:
                    swap_pos += 1
                    continue
                else:
                    row[swap_pos] = 'O'
                    row[x] = '.'
                    swap_pos += 1
            elif row[x] == '.':
                continue
            else:
                swap_pos = x+1


def calculate(mtx):
    accum = 0
    for i in range(len(mtx)):
        multiplier = len(mtx)
        for j in range(len(mtx[i])):
            if mtx[i][j] == 'O':
                accum += multiplier
                multiplier -= 1
            elif mtx[i][j] == '#':
                multiplier = len(mtx) - j - 1
    return accum


def run_cycle(mtx):
    # fix north -> transpose, swap, transpose
    to_return = transpose(copy.deepcopy(mtx))
    for row in to_return:
        row = swap(row, 0)
    to_return = transpose(to_return)

    # fix west -> swap
    for rr in to_return:
        row = swap(rr, 0)

    # fix south -> transpose, reverse swap, transpose
    to_return = transpose(to_return)
    for rr in to_return:
        row = swap(rr, 1)
    to_return = transpose(to_return)

    # fix east -> reverse swap
    for rr in to_return:
        row = swap(rr, 1)
    return to_return


def recurse(mtx, rotations):
    seen_matrices = []
    for i in range(rotations):
        mtx = run_cycle(mtx)
        if mtx in seen_matrices:
            cycle_period = i - seen_matrices.index(mtx)
            remaining = (rotations - i) % cycle_period - 1
            return recurse(mtx, remaining)
        else:
            seen_matrices.append(copy.deepcopy(mtx))
    return mtx


def solve(input_arr, part):
    orig = [list(row) for row in input_arr]
    changed = copy.deepcopy(orig)
    if part == 1:
        # transpose matrix.
        changed = transpose(changed)
        return calculate(changed)

    else:  # part 2 DOES NOT WORK
        rotator = 1_000_000_000
        changed = recurse(changed, rotator)

    return calculate(changed)


if __name__ == '__main__':
    text_arr = read_into_list('in_d14.txt')
    print(solve(text_arr, 1))
    print(solve(text_arr, 2))
