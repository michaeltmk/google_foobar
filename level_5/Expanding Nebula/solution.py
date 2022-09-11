encoded_list_0 = {
    "0000": {"up": "00", "down": "00", "left": "00", "right": "00"},
    "1100": {"up": "11", "down": "00", "left": "10", "right": "10"},
    "1010": {"up": "10", "down": "10", "left": "11", "right": "00"},
    "1001": {"up": "10", "down": "01", "left": "10", "right": "01"},
    "0110": {"up": "01", "down": "10", "left": "01", "right": "10"},
    "0101": {"up": "01", "down": "01", "left": "00", "right": "11"},
    "0011": {"up": "00", "down": "11", "left": "01", "right": "01"},
    "1110": {"up": "11", "down": "10", "left": "11", "right": "10"},
    "1101": {"up": "11", "down": "01", "left": "10", "right": "11"},
    "1011": {"up": "10", "down": "11", "left": "11", "right": "01"},
    "0111": {"up": "01", "down": "11", "left": "01", "right": "11"},
    "1111": {"up": "11", "down": "11", "left": "11", "right": "11"},
}
encoded_list_1 = {
    "1000": {"up": "10", "down": "00", "left": "10", "right": "00"},
    "0100": {"up": "01", "down": "00", "left": "00", "right": "10"},
    "0010": {"up": "00", "down": "10", "left": "01", "right": "00"},
    "0001": {"up": "00", "down": "01", "left": "00", "right": "01"},
}
encoded_list_0_ = {
    "00": [
        {"up": "00", "down": "00", "left": "00", "right": "00"},
        {"up": "00", "down": "11", "left": "01", "right": "01"},
    ],
    "11": [
        {"up": "11", "down": "00", "left": "10", "right": "10"},
        {"up": "11", "down": "10", "left": "11", "right": "10"},
        {"up": "11", "down": "01", "left": "10", "right": "11"},
        {"up": "11", "down": "11", "left": "11", "right": "11"},
    ],
    "10": [
        {"up": "10", "down": "10", "left": "11", "right": "00"},
        {"up": "10", "down": "01", "left": "10", "right": "01"},
        {"up": "10", "down": "11", "left": "11", "right": "01"},
    ],
    "01": [
        {"up": "01", "down": "10", "left": "01", "right": "10"},
        {"up": "01", "down": "01", "left": "00", "right": "11"},
        {"up": "01", "down": "11", "left": "01", "right": "11"},
    ],
}
encoded_list_1_ = {
    "10": [{"up": "10", "down": "00", "left": "10", "right": "00"}],
    "01": [{"up": "01", "down": "00", "left": "00", "right": "10"}],
    "00": [
        {"up": "00", "down": "10", "left": "01", "right": "00"},
        {"up": "00", "down": "01", "left": "00", "right": "01"},
    ],
}
init_set_of_previous_0 = {
    "00": [{"left": "00", "right": "00"}, {"left": "10", "right": "10"}],
    "10": [
        {"left": "11", "right": "00"},
        {"left": "01", "right": "10"},
        {"left": "11", "right": "10"},
    ],
    "01": [
        {"left": "10", "right": "01"},
        {"left": "00", "right": "11"},
        {"left": "10", "right": "11"},
    ],
    "11": [
        {"left": "01", "right": "01"},
        {"left": "11", "right": "01"},
        {"left": "01", "right": "11"},
        {"left": "11", "right": "11"},
    ],
}
init_set_of_previous_1 = {
    "00": [{"left": "10", "right": "00"}, {"left": "00", "right": "10"}],
    "10": [{"left": "01", "right": "00"}],
    "01": [{"left": "00", "right": "01"}],
}


def filling(set_of_previous, next_element, encoded_list_0, encoded_list_1):
    selected_encoded_list = encoded_list_0 if next_element == 0 else encoded_list_1
    new_set_of_previous = []
    if len(set_of_previous) == 0:
        return [[selected_encoded_list[k]] for k in selected_encoded_list.keys()]
    for sequence in set_of_previous:
        down = sequence[-1]["down"]
        for element in [selected_encoded_list[k] for k in selected_encoded_list.keys()]:
            if element["up"] == down:
                new_set_of_previous.append(sequence + [element])
    return new_set_of_previous


def filling2(set_of_previous, next_element, encoded_list_0, encoded_list_1):
    """
    aggregate the left and right of the previous column
    latest down as a key
    set_of_previous: {"00":[{"left":"00...0","right":"01...0"}], ...}
    encoded_lists use up as a key
    e.g. {"10": [{"up":"10","down":"01","left":"00","right":"01"}, ...], ...}
    next_element: 0 or 1
    """
    selected_encoded_list = encoded_list_0 if next_element == 0 else encoded_list_1
    new_set_of_previous = {}
    if len(set_of_previous) == 0:
        return init_set_of_previous_1 if next_element == 1 else init_set_of_previous_0
    for down, pre_v in set_of_previous.items():
        for basic_unit in selected_encoded_list.get(down, []):
            if not new_set_of_previous.get(basic_unit["down"]):
                new_set_of_previous[basic_unit["down"]] = []
            for left_right in pre_v:
                """
                basic_unit: {"up":"10","down":"01","left":"00","right":"01"}
                left_right: {"left":"00...0","right":"01...0"}
                new_set_of_previous: {"11":[{"left":"00...01","right":"01...01"}], ...}
                """
                left = left_right["left"] + basic_unit["left"]
                right = left_right["right"] + basic_unit["right"]
                new_set_of_previous[basic_unit["down"]].append(
                    {"left": left, "right": right}
                )
    return new_set_of_previous


def decode(encoded_column):
    """
    encoded_column: [{"up":"10","down":"01","left":"00","right":"01"}, ...]
    to
    result: {"left":"00...","right":"01..."}
    """
    left = []
    right = []
    for element in encoded_column:
        left.append(element["left"])
        right.append(element["right"])
    return {"left": "".join(left), "right": "".join(right)}


def dynamic_filling(past, next_ref):
    """
    past: {"1000": 10, "0100":2 , ...}
    next_ref: {"1000": ["1000"], "0100":["1001","0011"] , ...}
    """
    result = {}
    for past_e, past_v in past.items():
        if next_ref.get(past_e):
            for next_e in next_ref[past_e]:
                result[next_e] = result.get(next_e, 0) + past_v
    return result


def multi_decode(encoded_columns):
    """
    encoded_columns: [
            [{"up":"10","down":"01","left":"00","right":"01"}, ...],
            [{"up":"10","down":"01","left":"01","right":"11"}, ...],
            ...
        ]
    to
    result: {"1000": ["1000"], "0100":["1001","0011"] , ...}
    """
    result = {}
    for encoded_column in encoded_columns:
        code = decode(encoded_column)
        result[code["left"]] = result.get(code["left"], []) + [code["right"]]
    return result


def multi_decode2(encoded_columns):
    """
    encoded_columns: [{"left":"00...","right":"01..."}, ...]
    to
    result: {"1000": ["1000"], "0100":["1001","0011"] , ...}
    """
    result = {}
    for encoded_column in encoded_columns:
        if not result.get(encoded_column["left"]):
            result[encoded_column["left"]] = []
        result[encoded_column["left"]].append(encoded_column["right"])
    return result


def initial_past(encoded_columns):
    """
    right as the key
    encoded_columns: [
            [{"up":"10","down":"01","left":"00","right":"01"}, ...],
            [{"up":"10","down":"01","left":"01","right":"11"}, ...],
            ...
        ]
    to
    result: {"1000": 2, "0100":3 , ...}
    """
    result = {}
    for column in encoded_columns:
        right = decode(column)["right"]
        result[right] = result.get(right, 0) + 1
    return result


def initial_past2(encoded_columns):
    """
    right as the key
    encoded_columns: [{"left":"00...","right":"01..."}, ...]
    to
    result: {"1000": 2, "0100":3 , ...}
    """
    result = {}
    for column in encoded_columns:
        right = column["right"]
        result[right] = result.get(right, 0) + 1
    return result


def flatten(columns):
    """
    columns: {"00":[{"left":"00...","right":"01..."}, ...], ...}
    to
    result: [{"left":"00...","right":"01..."},...]
    """
    result = []
    for v in columns.values():
        result += v
    return result


def set_of_previous_1d(current_column, encoded_list_0, encoded_list_1):
    set_of_previous = []
    for e in current_column:
        set_of_previous = filling(set_of_previous, e, encoded_list_0, encoded_list_1)
    return set_of_previous


def set_of_previous_1d2(current_column, encoded_list_0, encoded_list_1):
    set_of_previous = []
    for e in current_column:
        set_of_previous = filling2(set_of_previous, e, encoded_list_0, encoded_list_1)
    return flatten(set_of_previous)


def solution(list_list):
    # special care first column as we need to initial the past
    first_column = list_list[0]
    past = initial_past(
        set_of_previous_1d(first_column, encoded_list_0, encoded_list_1)
    )

    grid = []
    for current_column in list_list[1:]:
        grid.append(
            multi_decode(
                set_of_previous_1d(current_column, encoded_list_0, encoded_list_1)
            )
        )

    # compute the possible solutions
    for next_ref in grid:
        past = dynamic_filling(past, next_ref)
    return sum(past.values())


def solution2(list_list):
    # special care first column as we need to initial the past
    first_column = list_list[0]
    past = initial_past2(
        set_of_previous_1d2(first_column, encoded_list_0_, encoded_list_1_)
    )

    grid = []
    for current_column in list_list[1:]:
        grid.append(
            multi_decode2(
                set_of_previous_1d2(current_column, encoded_list_0_, encoded_list_1_)
            )
        )

    # compute the possible solutions
    print(past)
    print(grid)
    for next_ref in grid:
        past = dynamic_filling(past, next_ref)
    return sum(past.values())
