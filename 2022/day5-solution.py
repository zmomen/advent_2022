import os


def part2():
    with open(os.getcwd() + '/2022/input/adventofcode.com_2022_day_5_input.txt', 'r') as file:
        read_stacks = 0
        st = []
        for i in range(9):
            st.append([])

        finished_stacks = False
        for line in file:
            if not finished_stacks:
                # read values in all stacks 
                if read_stacks < 8:
                    read_stacks += 1

                    seeker = 0
                    inp = line.replace('\n', '')
                    while seeker < len(inp):
                        if inp[seeker:seeker+4].strip() == '':
                            seeker += 4
                            continue
                        else:
                            st[((seeker + 4) // 4)-1].append(inp[seeker+1])
                            seeker += 4
                else:
                    file.readline()
                    for i in range(9):
                        st[i].reverse()
                    finished_stacks = True
            else:
                # actions
                actions = line.split(' ')
                how_many = int(actions[1])
                from_stack = int(actions[3])-1
                to_stack = int(actions[5])-1

                st[to_stack].extend(st[from_stack][-how_many:])
                st[from_stack] = st[from_stack][:-how_many]
        res = ''
        for i in range(9):                
            res += st[i][-1]
        print(res)    


def part1():
    with open(os.getcwd() + '/2022/input/adventofcode.com_2022_day_5_input.txt', 'r') as file:
        read_stacks = 0
        st = []
        for i in range(9):
            st.append([])

        finished_stacks = False
        for line in file:
            if not finished_stacks:
                # read values in all stacks 
                if read_stacks < 8:
                    read_stacks += 1

                    seeker = 0
                    inp = line.replace('\n', '')
                    while seeker < len(inp):
                        if inp[seeker:seeker+4].strip() == '':
                            seeker += 4
                            continue
                        else:
                            st[((seeker + 4) // 4)-1].append(inp[seeker+1])
                            seeker += 4
                else:
                    file.readline()
                    for i in range(9):
                        st[i].reverse()
                    print(st)
                    finished_stacks = True
            else:
                # actions
                actions = line.split(' ')
                how_many = int(actions[1])
                from_stack = int(actions[3])-1
                to_stack = int(actions[5])-1
                print(actions, how_many, from_stack, to_stack)
                for i in range(how_many):
                    st[to_stack].append(st[from_stack].pop())

        res = ''
        for i in range(9):                
            res += st[i][-1]
        print(res)        


part1()
part2()
