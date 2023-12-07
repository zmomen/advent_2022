from typing import List

from utils import read_into_list


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # sort intervals by first in each range.
    # starting with 2nd. if start in betwen last's ranges take min starts and max ends.

    if len(intervals) == 1:
        return intervals
    sorted_arr = sorted(intervals, key=lambda x: x[0])
    # print(sorted_arr)

    i = 1

    while i < len(sorted_arr):
        if sorted_arr[i-1][0] <= sorted_arr[i][0] <= sorted_arr[i-1][1]:
            nn = min(sorted_arr[i-1][0], sorted_arr[i][0])
            mm = max(sorted_arr[i-1][1], sorted_arr[i][1])
            sorted_arr[i][0] = nn
            sorted_arr[i][1] = mm
            sorted_arr.pop(i-1)
            i -= 1
        i += 1

    if len(sorted_arr) > 1:
        if sorted_arr[-2][0] <= sorted_arr[-1][0] <= sorted_arr[-2][1]:
            nn = min(sorted_arr[-2][0], sorted_arr[-1][0])
            mm = max(sorted_arr[-2][1], sorted_arr[-1][1])
            sorted_arr[-1][0] = nn
            sorted_arr[-1][1] = mm
            sorted_arr.pop(-2)

    return sorted_arr


def solve(lines, part):
    seed_line = list(map(int, lines[0].split(" ")[1:]))
    title_order = []
    maps = {}
    title = ""
    for line in lines:
        if len(line.strip()) == 0 or "seeds" in line:
            continue
        elif "map" in line:
            title = line.split(" ")[0]
            title_order.append(title)
            maps[title] = []
        else:
            maps[title].append(list(map(int, line.strip().split(" "))))
    min_loc = float('inf')
    if part == 1:
        for key_to_check in seed_line:
            for box in title_order:
                for liner in maps[box]:
                    if key_to_check >= liner[1] and key_to_check <= liner[1]+liner[2]:
                        key_to_check = liner[0] + abs(key_to_check-liner[1])
                        break
            min_loc = min(min_loc, key_to_check)
    else:
        new_seeds = [[seed_line[i], seed_line[i]+seed_line[i+1]]
                     for i in range(0, len(seed_line), 2)]

        new_ranges = [[124747783, 357574820], [
            481035699, 2540043860], [2578953067, 5185268764]]
        # slow
        for i in range(len(new_ranges)):
            rrange = new_ranges[i]
            for key_to_check in range(rrange[0], rrange[1]):
                for box in title_order:
                    for liner in maps[box]:
                        if key_to_check >= liner[1] and key_to_check <= liner[1]+liner[2]:
                            key_to_check = liner[0] + \
                                abs(key_to_check-liner[1])
                            break
                min_loc = min(min_loc, key_to_check)

    return min_loc

    # 7 checks.
    # a check of key in range
    # range is second digit  between (start_range, start_range + range_length)
    # if found in line, get the first digit(dest) + abs(key-start_range)
    # this becomes the new key for next step.
    # keep going until location.
    # track min location.
if __name__ == '__main__':
    text_arr = read_into_list('in_d5.txt')
    # print(solve(text_arr, 1))
    print(solve(text_arr, 2))
