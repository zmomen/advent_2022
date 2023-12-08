from collections import Counter, defaultdict

from utils import read_into_list

# read hands into array of Hand classes.
# create a compare function that sorts two hands based on strength of hand and of card.
# each hand has a strength based on criteria of the hand.
# each card in hand has a strength.

card_guide = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

hand_guide = {
    "Five": 5.0,
    "Four": 4.0,
    "Full": 3.5,
    "Three": 3.0,
    "Two": 2.0,
    "One": 1.0,
    "High": 0.0,
}


class Hand:
    def __init__(self, hand_str, init_part=1) -> None:
        self.hand_str = hand_str
        self.hand_type = None
        self.card_values = None

        if init_part == 1:
            self.parse_into_hand_type_p1()
        else:
            self.parse_into_hand_type_p2()
        self.get_card_values(init_part)

    def get_hand_str(self) -> str:
        return self.hand_str

    def parse_into_hand_type_p1(self):
        temp = dict(Counter(self.hand_str))
        if 5 in temp.values():
            self.hand_type = hand_guide["Five"]
        elif 4 in temp.values():
            self.hand_type = hand_guide["Four"]
        elif 3 in temp.values() and 2 in temp.values():
            self.hand_type = hand_guide["Full"]
        elif 3 in temp.values():
            self.hand_type = hand_guide["Three"]
        elif len(temp.values()) == 3 and 2 in temp.values():
            self.hand_type = hand_guide["Two"]
        elif len(temp.values()) == 4 and 2 in temp.values():
            self.hand_type = hand_guide["One"]
        else:
            self.hand_type = hand_guide["High"]

    def parse_into_hand_type_p2(self):
        temp = dict(Counter(self.hand_str))
        if 5 in temp.values():
            self.hand_type = hand_guide["Five"]
        elif 4 in temp.values():
            if 'J' in temp:  # j4444 jjjj4
                self.hand_type = hand_guide["Five"]
            else:
                self.hand_type = hand_guide["Four"]
        elif 3 in temp.values() and 2 in temp.values():
            if 'J' in temp:  # 444jj jjj44
                self.hand_type = hand_guide["Five"]
            else:
                self.hand_type = hand_guide["Full"]
        elif 3 in temp.values():  # jjj49, 99j94 = 99948
            if 'J' in temp:
                self.hand_type = hand_guide["Four"]
            else:
                self.hand_type = hand_guide["Three"]
        elif len(temp.values()) == 3 and 2 in temp.values():  # 2,2,1 4499t 44jtt jj44t
            if 'J' in temp and temp['J'] == 2:
                self.hand_type = hand_guide["Four"]
            elif 'J' in temp and temp['J'] == 1:
                self.hand_type = hand_guide["Full"]
            else:
                self.hand_type = hand_guide["Two"]
        elif len(temp.values()) == 4 and 2 in temp.values():  # 2,1,1,1 jj46t 4t99j 44326
            if 'J' in temp:
                self.hand_type = hand_guide["Three"]
            else:
                self.hand_type = hand_guide["One"]
        elif 'J' in temp:  # 3456j
            self.hand_type = hand_guide["One"]
        else:
            self.hand_type = hand_guide["High"]

    def get_card_values(self, part):
        if part == 2:
            card_guide["J"] = 1
        self.card_values = [card_guide[x] for x in list(self.hand_str)]


def solve(input_arr, part):
    hands_values = {}
    list_of_hands = []
    for line in input_arr:
        splitter = line.split(' ')
        hands_values[splitter[0]] = int(splitter[1])
        list_of_hands.append(Hand(splitter[0], part))

    list_of_hands.sort(key=lambda hand: hand.hand_type)

    # second sort by card values only for those hands that have equal hand values.
    to_sort = {}
    i = 0
    j = i+1
    while i < len(list_of_hands)-1 and j < len(list_of_hands):
        if list_of_hands[i].hand_type == list_of_hands[j].hand_type:
            if i in to_sort:
                to_sort[i].append(list_of_hands[j])
            else:
                to_sort[i] = [list_of_hands[i], list_of_hands[j]]
            j += 1
        else:
            i = j
            j = i+1

    for k, v in to_sort.items():
        v.sort(key=lambda x: x.card_values)
        for i in range(len(v)):
            list_of_hands[k+i] = v[i]

    total_winnings = 0
    for i in range(len(list_of_hands)):
        total_winnings += (i+1) * hands_values[list_of_hands[i].hand_str]

    return total_winnings


if __name__ == '__main__':
    text_arr = read_into_list('in_d7.txt')
    print(solve(text_arr, 1))
    print(solve(text_arr, 2))
