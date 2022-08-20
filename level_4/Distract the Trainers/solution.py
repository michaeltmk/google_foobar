import math
import collections

def use_matrix(r_of_mode_n):
    '''use matrix to determinate num_bored_trainer'''
    grouping_matrix = [[-2 for _ in range(len(r_of_mode_n))] for _ in range(len(r_of_mode_n))]
    # print(f'{grouping_matrix=}')
    # init of a lower triangular matrix
    for i in range(len(r_of_mode_n)):
        for j in range(len(r_of_mode_n)-i):
            grouping_matrix[i][i+j] = 2 #use 2 to prevent mixing with following steps
    # print(f'{grouping_matrix=}')
    
    #check isInfiniteLoop for all elements with 0 value, if no, then set value to 1
    for i in range(len(r_of_mode_n)):
        for j in range(len(r_of_mode_n)):
            if grouping_matrix[i][j] == -2:
                if isInfiniteLoop(r_of_mode_n[i],r_of_mode_n[j]):
                    grouping_matrix[i][j] = 0
                    grouping_matrix[j][i] = 0
                    #changing all elements in the same row and column to -1
                    for k in range(len(r_of_mode_n)):
                        if grouping_matrix[i][k] == -2:
                            grouping_matrix[i][k] = -1
                            grouping_matrix[k][i] = -1
                        if grouping_matrix[j][k] == -2:
                            grouping_matrix[j][k] = -1
                            grouping_matrix[k][j] = -1
                    break
                else:
                    grouping_matrix[i][j] = 1
                    grouping_matrix[j][i] = 1
    # print(f'{grouping_matrix=}')
    #find which row have no isInfiniteLoop, search those -1 in the row
    for i in range(len(r_of_mode_n)):
        if grouping_matrix[i].count(0) == 0:
            for j in range(len(r_of_mode_n)):
                if grouping_matrix[i][j] == -1:
                    if isInfiniteLoop(r_of_mode_n[i],r_of_mode_n[j]):
                        grouping_matrix[i][j] = 0
                        grouping_matrix[j][i] = 0
                        break
                    else:
                        grouping_matrix[i][j] = 1
                        grouping_matrix[j][i] = 1

    #check how many row have no 0
    num_bored_trainer = 0
    for i in range(len(r_of_mode_n)):
        if grouping_matrix[i].count(0) == 0:
            num_bored_trainer += 1
    return num_bored_trainer

def solution(banana_list):
    n_list = []
    nr_list = []
    for x in banana_list:
        n,r = find_greatest_odd_factor(x)
        n_list.append(n)
        nr_list.append((n,r))
    data_dict = dict(collections.Counter(n_list))
    max_freq = max(list(data_dict.values()))
    # print(f'{max_freq=}')
    if max_freq < len(banana_list)/2:
        return 0 if len(banana_list)%2 == 0 else 1
    else:
        mode_n = [num for num, freq in data_dict.items() if freq == max_freq]
        # assert len(mode_n) == 1
        r_of_mode_n = [r for n,r in nr_list if n in mode_n]
        # print(f'{r_of_mode_n=}')
        num_bored_trainer = use_matrix(r_of_mode_n)
        #for those r which cannot find a r2, ie they are bored,those r can be matched with other r which is not mode_n
        result = max([num_bored_trainer - (len(banana_list)-max_freq),0]) 
        return result if len(banana_list)%2 == 0 else result+1

    
def find_greatest_odd_factor(x):
    '''Find the greatest odd factor of x
    return (n,r) where x = (2^n)*r'''
    n = 0
    while x%2 == 0:
        n += 1
        x = x/2
    return (n,int(x))


def isInfiniteLoop(a,b):
    # print(f"now checking {a} and {b}")
    if a == b:
        return False
    elif (a+b)%2 !=0:
        # print("not even")
        return True
    else:
        if math.log(a+b,2)%1 == 0:
            # print("is 2^n")
            return False
        else:
            # print(f'log({a+b},2)%1 = {math.log(a+b,2)%1}')
            v = (a+b)/2
            # print(f"{v=}")
            while True:
                if v%2 != 0:
                    break
                else:
                    v = v/2
            if a%v == 0:
                # print(f'{a}%{v} = 0')
                return False
            else:
                # print(f'{a}%{v} = {a%v}')
                return True
