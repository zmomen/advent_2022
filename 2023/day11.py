from utils import read_into_list


def manhattan_distance(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return abs(x2 - x1) + abs(y2 - y1)


def solve(input_arr, part):
    larger_by = 1000_000
    spaces = []
    empty_rows = []
    empty_cols = []
    # read and find empty rows and cols
    for line in input_arr:
        spaces.append(list(line.strip()))
        if "#" not in spaces[-1]:
            empty_rows.append(len(spaces) - 1)

    for j in range(len(spaces)):
        empty_c = True
        for i in range(len(spaces)):
            if spaces[i][j] == "#":
                empty_c = False
                break
        if empty_c:
            empty_cols.append(j)

    if part == 1:
        i = 0
        for good_row in empty_rows:
            spaces.insert(good_row+i, spaces[good_row+i])
            i += 1

        j = 0
        for good_col in empty_cols:
            for row in spaces:
                row.insert(good_col+j, '.')
            j += 1

    # print("rows", empty_rows)
    # print("cols", empty_cols)

    glx = []
    for i in range(len(spaces)):
        for j in range(len(spaces[i])):
            if spaces[i][j] == "#":
                glx.append([i, j])
    sums = 0
    for i in range(len(glx)):
        for j in range(i + 1, len(glx)):
            position1 = glx[i]
            position2 = glx[j]
            distance = 0
            if part == 2:
                for emp in empty_rows:
                    if emp > min(position1[0], position2[0]) and emp < max(position1[0], position2[0]):
                        distance = distance + larger_by - 1
                
                for emp in empty_cols:
                    if emp > min(position1[1], position2[1]) and emp < max(position1[1], position2[1]):
                        distance = distance + larger_by - 1
                
            distance += manhattan_distance(position1, position2)
            sums += distance
    return sums


if __name__ == '__main__':
    text_arr = read_into_list('in_d11.txt')
    print(solve(text_arr, 1))
    print(solve(text_arr, 2))
