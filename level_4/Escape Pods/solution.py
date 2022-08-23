def solution(entrances, exits, path):
    pass

def combine_multirow(rows:list):
    '''1d matrix addition, must be same length'''
    result = [0 for x in range(len(rows[0]))]
    for row in rows:
        for i in range(len(row)):
            result[i]+=row[i]

    return result
