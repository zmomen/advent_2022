from utils import read_into_list


def solve(input_arr, part):

    cards = []
    for line in input_arr:
        # Split the line into card name and numbers
        card_name, numbers_str = line.split(':')
        card_name = int(card_name.strip().split(' ')[-1])

        # Split numbers into winning and numbers
        winning_str, numbers_str = map(str.strip, numbers_str.split('|'))
        winning = list(map(int, winning_str.split()))
        numbers = list(map(int, numbers_str.split()))

        # Create a dictionary for the current card
        card_dict = {'card_name': card_name,
                     'winning': winning, 'numbers': numbers}

        # Append the dictionary to the list of cards
        cards.append(card_dict)

    allTotal = 0
    jumper = {}
    queue = []

    for card in cards:
        curTotal = 0
        found = 0
        copies = []
        for winner in card['winning']:
            if winner in card['numbers']:
                curTotal = pow(2, found)
                found += 1
                queue.append(found+card['card_name'])
                copies.append(found+card['card_name'])
        allTotal += curTotal
        jumper[card['card_name']] = copies

    if part == 1:
        return allTotal
    else:  # part 2
        cur = 0
        while cur < len(queue):
            queue.extend(jumper[queue[cur]])
            cur += 1
        return len(queue) + len(jumper.keys())


if __name__ == '__main__':
    text_arr = read_into_list('in_d4.txt')
    print(solve(text_arr, 1))
    print(solve(text_arr, 2))
