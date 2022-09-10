
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

def set_of_previous_1d(current_column,encoded_list_0, encoded_list_1):
    set_of_previous = []
    for e in current_column:
        set_of_previous = filling(set_of_previous, e, encoded_list_0, encoded_list_1)
    return set_of_previous

def solution(list_list):
    pass