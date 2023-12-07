import os

def read_into_list(filename):
    with open(os.getcwd() + '/2023/input/' + filename, 'r') as file:
        return [line.strip() for line in file]
