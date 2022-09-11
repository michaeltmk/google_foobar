
basic_unit_return_0 = ["0000","1100","1010","1001","0110","0101","0011","1110","1101","1011","0111","1111"]
basic_unit_return_1 = ["1000","0100","0010","0001"]
def encode_list_to_int(basic_units):
    result = {}
    for basic_unit in basic_units:
        # up = int(basic_unit[:2],2)
        # down = int(basic_unit[2:],2)
        up = basic_unit[:2]
        down = basic_unit[2:]
        left = basic_unit[0] + basic_unit[2]
        right = basic_unit[1] + basic_unit[3]
        result[basic_unit] = {"up":up,"down":down,"left":left,"right":right}
    return result
encoded_list_0 = encode_list_to_int(basic_unit_return_0)
encoded_list_1 = encode_list_to_int(basic_unit_return_1)

def filling(set_of_previous, next_element,encoded_list_0, encoded_list_1):
    selected_encoded_list = encoded_list_0 if next_element == 0 else encoded_list_1
    new_set_of_previous = []
    if len(set_of_previous) == 0:
        return [[selected_encoded_list[k]] for k in selected_encoded_list.keys()]
    for sequence in set_of_previous:
        down = sequence[-1]["down"]
        for element in [selected_encoded_list[k] for k in selected_encoded_list.keys()]:
            if element["up"] == down:
                new_set_of_previous.append(sequence+[element])
    return new_set_of_previous

def decode(encoded_column):
    '''
        encoded_column: [{"up":"10","down":"01","left":"00","right":"01"}, ...]
        to
        result: {"left":"00...","right":"01..."}
    '''
    left = []
    right = []
    for element in encoded_column:
        left.append(element["left"])
        right.append(element["right"])
    return {"left":"".join(left), "right":"".join(right)}

def dynamic_filling(past, next_ref):
    '''
        past: {"1000": 10, "0100":2 , ...}
        next_ref: {"1000": ["1000"], "0100":["1001","0011"] , ...}
    '''
    result = {}
    for past_e, past_v in past.items():
        if next_ref.get(past_e):
            for next_e in next_ref[past_e]:
                result[next_e] = result.get(next_e,0) + past_v
    return result

def multi_decode(encoded_columns):
        '''
        encoded_columns: [
                [{"up":"10","down":"01","left":"00","right":"01"}, ...],
                [{"up":"10","down":"01","left":"01","right":"11"}, ...],
                ...
            ]
        to
        result: {"1000": ["1000"], "0100":["1001","0011"] , ...}
        '''
        result = {}
        for encoded_column in encoded_columns:
            code = decode(encoded_column)
            result[code['left']] = result.get(code['left'],[]) + [code['right']]
        return result

def initial_past(encoded_columns):
    '''
        right as the key
        encoded_columns: [
                [{"up":"10","down":"01","left":"00","right":"01"}, ...],
                [{"up":"10","down":"01","left":"01","right":"11"}, ...],
                ...
            ]
        to
        result: {"1000": 2, "0100":3 , ...}
    '''
    result = {}
    for column in encoded_columns:
        right = decode(column)['right']
        result[right] = result.get(right,0) + 1
    return result

def set_of_previous_1d(current_column,encoded_list_0, encoded_list_1):
    set_of_previous = []
    for e in current_column:
        set_of_previous = filling(set_of_previous, e, encoded_list_0, encoded_list_1)
    return set_of_previous

def solution(list_list):
    #special care first column as we need to initial the past
    first_column = list_list[0]
    past = initial_past(set_of_previous_1d(first_column,encoded_list_0, encoded_list_1))

    grid = []
    for current_column in list_list[1:]:
        grid.append(multi_decode(set_of_previous_1d(current_column,encoded_list_0, encoded_list_1)))
    
    #compute the possible solutions
    for next_ref in grid:
        past = dynamic_filling(past, next_ref)
    return sum(past.values())