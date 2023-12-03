import os


def read():
    return open(os.getcwd() + '/2023/input/in_d2p1.txt', 'r')


def solve(textfile, part):
    part2_totals = 0    
    games = 0
    for line in textfile:
        line_split = line.split(":")
        game_id = int(line_split[0].split(" ")[1])
        subs = line_split[1].split(";")
        
        is_good = True
        game_totals = {"red": 0, "green": 0, "blue": 0}

        for sub in subs:
            color_totals = {"red": 0, "green": 0, "blue": 0}
            for color in sub.split(","):
                color = color.strip()
                ball_count = int(color.split(" ")[0])
                col = color.split(" ")[1]
                color_totals[col] = ball_count
                if ball_count > game_totals[col]:
                    game_totals[col] = ball_count

            if part == 1:    
                if color_totals["red"] > 12 \
                    or color_totals["green"] > 13 \
                        or color_totals["blue"] > 14:
                    is_good = False
                    break
        part2_totals += game_totals["red"] * game_totals["green"] * game_totals["blue"]
        if is_good:
            games+=game_id
    
    return games if part == 1 else part2_totals


if __name__ == '__main__':
    textfile = read()
    # print(solve(textfile, 1))
    print(solve(textfile, 2))


def solve(text):
    total_p1 = 0
    total_p2 = 0
    for line in text.split("\n"):
        found = {"red": [0, 12], "green": [0, 13], "blue": [0, 14]}
        game_id = line.split()[1].split(":")[0]
        games = line.split(":")[1].split(";")
        for game in games:
            for dice in game.split(","):
                val, color = dice.split()
                if int(val) > found[color][0]:
                    found[color][0] = int(val.strip())
        if all(found[color][0] <= found[color][1] for color in found):
            total_p1 += int(game_id)
        total_p2 += found["red"][0] * found["green"][0] * found["blue"][0]
    return total_p1, total_p2