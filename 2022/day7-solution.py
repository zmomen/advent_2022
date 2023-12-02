import os 
# credit: https://github.com/PodolskiBartosz/advent-of-code-2022/blob/main/day-7/main.py

def main():
    print("Advent of Code - Day 7")
    file_task_1 = open(os.getcwd() + '/2022/input/adventofcode.com_2022_day_7_input.txt', 'r') 
    file_task_2 = open(os.getcwd() + '/2022/input/adventofcode.com_2022_day_7_input.txt', 'r') 
    task_1(file_task_1)
    task_2(file_task_2)


def get_file_system_directories(file):
    # Create a list of directories by judging the inputs
    current_path = ""
    directories = {"/home": 0}
    for line in file.read().splitlines():
        line = line.split()
        if line[0] == "$":
            if line[1] == "ls":
                pass
            else:
                if line[2] == "..":
                    # Find index of last occurrence of "/" and create new string up until that index
                    current_path = current_path[:current_path.rindex("/")]
                elif line[2] == "/":
                    current_path = "/home"
                else:
                    current_path = current_path + "/" + line[2]
                    directories[current_path] = 0
        else:
            if line[0] != "dir":
                temp_path = current_path
                # Update all parent directories
                while temp_path != "":
                    directories[temp_path] += int(line[0])
                    temp_path = temp_path[:temp_path.rindex("/")]
    return directories


# Task 1: Get sum of all directories with a total size of at most 100000
def task_1(file):
    directories = get_file_system_directories(file)
    sum_small_directories = 0
    for _, directory in directories.items():
        if directory < 100000:
            sum_small_directories += directory
    print("Task 1 result: " + str(sum_small_directories))


# Task 2: Get the smallest directory that can be deleted, in order to have at least 30000000 free space, with 70000000
#         being the total disk space available
def task_2(file):
    directories = get_file_system_directories(file)
    required_free_space = directories["/home"] - (70000000 - 30000000)  # 40000000 of the space can be used
    smallest_deletable_directory = directories["/home"]
    for _, directory in directories.items():
        if required_free_space < directory < smallest_deletable_directory:
            smallest_deletable_directory = directory
    print("Task 1 result: " + str(smallest_deletable_directory))


if __name__ == "__main__":
    main()
    





# # create a hash table of objects.
# # read each line. if ls (stay on hash key and insert into it. )
# # cd use stack and push. cd.. pop.

# import os


# def create_dict():
#     with open(os.getcwd() + '/2022/input/adventofcode.com_2022_day_7_input.txt', 'r') as file:
#         curpath = []
#         dc = {}
#         while True:
#             line = file.readline().strip()
#             if not line:
#                 break
#             if "cd /" in line:
#                 curpath.append("/")
#                 dc["/"] = []
#                 pos = "/"
#                 file.readline()  # ls
#             elif "cd .." in line:
#                 curpath.pop()  # remove current
#                 pos = curpath[-1]  # go up
#             elif "cd" in line:
#                 pos = "dir " + line.split(" ")[-1]
#                 curpath.append(pos)
#                 file.readline()  # ls
#             elif "dir" in line:
#                 dc[pos].append(line)
#                 dc[line] = []
#             else:
#                 key = line.split(" ")[-1]
#                 val = line.split(" ")[0]
#                 dc[pos].append(key)
#                 dc[key] = val
#     return dc

# # curpath = stack [/, d]
# # {"/": ["dir a", "b.txt", "c.dat", "dir d"],
# #  "dir a": ["dir e", "f", "g", "h.lst"],
# #  "b.txt": 14848514,
# #  "c.dat": 8504156,
# #  "dir d": ["j", "d.log", "d.ext"],
# #  "dir e": ["i"],
# #  "i": 584
# #  "j": 4060174,
# #  "d.log": 8033020,
# #  "d.ext": 5626152,
# #  "k": 7214296
# #  }


# def calc_size_max(dictt):
#     copy = dictt.copy()
#     sizes = {}
#     total = 0
#     curpath = ["/"] # ["/", "dir a", "dir e"]
#     pos = copy["/"].pop(0)
#     while len(copy["/"]) >= 0:
#         if "dir" in pos or "/" in pos:
#             curpath.append(pos)
#             if len(copy[pos]) > 0:
#                 pos = copy[pos].pop(0)
#             else:
#                 sizes[pos] = total
#                 curpath.pop()
#                 pos = curpath.pop()
#                 if pos not in sizes: 
#                     sizes[pos] = total
#                     total = 0
#         else:
#             total += int(copy[pos])
#             pos = curpath.pop()


# if __name__ == "__main__":
#     dc = create_dict()
#     calc_size_max(dc)
