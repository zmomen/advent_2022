from utils import read_into_list


def solve(input_arr, part):
    times = list(map(int, input_arr[0].split()[1:]))
    distances = list(map(int, input_arr[1].split()[1:]))
    
    if part == 2:
        times = [int(''.join(str(x) for x in times))]
        distances = [int(''.join(str(x) for x in distances))]
        

    # first divide distance by time to get a starting point. 
    # calc first multiplier which is time minus starting point
    # second multiplier which is starting point
    # loop while decrementing first mult and incremening second. 
    # stop until total exceeds distance. 
    # calculate all ways to win by subtracting digits. 
    # get total accumulator from each race. 

    ways_to_win_race = 1
    for race in range(len(times)):
        starting_point = distances[race] // times[race]
        first_mult = times[race] - starting_point
        second_mult = starting_point
        while first_mult * second_mult <= distances[race]:
            first_mult-=1 
            second_mult+=1
        ways_to_win_race *= first_mult - second_mult + 1
    
    return ways_to_win_race


if __name__ == '__main__':
    text_arr = read_into_list('in_d6.txt')
    print(solve(text_arr, 1))
    print(solve(text_arr, 2))
