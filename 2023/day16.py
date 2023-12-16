import copy

from utils import read_into_list


def solve(input_arr, part):
    matrix = []
    for line in input_arr:
        matrix.append(list(line))

    rows = len(matrix)
    cols = len(matrix[0])

    directions = {
        '.right': {"pos": (0, 1), "direction": "right"},
        '/right': {"pos": (-1, 0), "direction": "up"},
        '\\right': {"pos": (1, 0), "direction": "down"},
        '-right': {"pos": (0, 1), "direction": "right"},
        '|right': {"pos": (0, 0), "direction": "split"},
        '.left': {"pos": (0, -1), "direction": "left"},
        '/left': {"pos": (1, 0), "direction": "down"},
        '\\left': {"pos": (-1, 0), "direction": "up"},
        '-left': {"pos": (0, -1), "direction": "left"},
        '|left': {"pos": (0, 0), "direction": "split"},
        '.up': {"pos": (-1, 0), "direction": "up"},
        '/up': {"pos": (0, 1), "direction": "right"},
        '\\up': {"pos": (0, -1), "direction": "left"},
        '-up': {"pos": (0, 0), "direction": "split"},
        '|up': {"pos": (-1, 0), "direction": "up"},
        '.down': {"pos": (1, 0), "direction": "down"},
        '/down': {"pos": (0, -1), "direction": "left"},
        '\\down': {"pos": (0, 1), "direction": "right"},
        '-down': {"pos": (0, 0), "direction": "split"},
        '|down': {"pos": (1, 0), "direction": "down"},
    }
    
    arrays = []
    max_val = 0
    if part == 1:
        # one starting position. 
        arrays = [{'pos': (0, 0), 'direction': 'right'}]
    else: 
        # generate array of starting positions. 
        # first and last rows
        for posit in range(cols):
            arrays.append({'pos': (0, posit), 'direction': 'down'})
            arrays.append({'pos': (rows-1, posit), 'direction': 'up'})
        # first and last columns
        for posit in range(rows):
            arrays.append({'pos': (posit, 0), 'direction': 'right'})
            arrays.append({'pos': (posit, cols-1), 'direction': 'left'})    
    
    for starting_pos in arrays:
        visited = [[False] * cols for _ in range(rows)]
        queue = [starting_pos]
        seen = set()
        while queue:
            coord = queue.pop(0)

            x = coord["pos"][0]
            y = coord["pos"][1]
            # check for out of bounds.
            if x < 0 or x >= rows or y < 0 or y >= cols:
                continue

            # if seen this direction before, exit.
            if str(coord["pos"]) + coord["direction"] in seen:
                continue 
            else: 
                seen.add(str(coord["pos"]) + coord["direction"])

            symbol = matrix[x][y]
            visited[x][y] = True

            next_pos = directions[symbol+coord["direction"]]

            # check for splits.
            # if right or left split. up and down
            if coord["direction"] in ['right', 'left'] and next_pos['direction'] == 'split':
                going_up_pos = {"pos": (x + next_pos["pos"][0] - 1, y + next_pos["pos"][1]),
                                "direction": "up"}
                going_down_pos = {"pos": (x + next_pos["pos"][0] + 1, y + next_pos["pos"][1]),
                                "direction": "down"}
                queue.extend([going_up_pos, going_down_pos])

            # else if up or down split. left and right
            elif coord["direction"] in ['up', 'down'] and next_pos['direction'] == 'split':
                going_left_pos = {"pos": (x + next_pos["pos"][0], y + next_pos["pos"][1] - 1),
                                "direction": "left"}
                going_right_pos = {"pos": (x + next_pos["pos"][0], y + next_pos["pos"][1] + 1),
                                "direction": "right"}
                queue.extend([going_left_pos, going_right_pos])

            # else normal next position
            else:
                queue.append({"pos": (x + next_pos["pos"][0], y + next_pos["pos"][1]),
                            "direction": next_pos["direction"]})

        max_val = max(max_val, sum(1 for row in visited for col in row if col > 0))
    
    return max_val


if __name__ == '__main__':
    text_arr = read_into_list('in_d16.txt')
    print(solve(text_arr, 1))
    print(solve(text_arr, 2))
