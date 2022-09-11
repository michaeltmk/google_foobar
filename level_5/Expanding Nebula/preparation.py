basic_unit_return_0 = [
    "0000",
    "1100",
    "1010",
    "1001",
    "0110",
    "0101",
    "0011",
    "1110",
    "1101",
    "1011",
    "0111",
    "1111",
]
basic_unit_return_1 = ["1000", "0100", "0010", "0001"]


def encode_list_to_int(basic_units):
    result = {}
    for basic_unit in basic_units:
        # up = int(basic_unit[:2],2)
        # down = int(basic_unit[2:],2)
        up = basic_unit[:2]
        down = basic_unit[2:]
        left = basic_unit[0] + basic_unit[2]
        right = basic_unit[1] + basic_unit[3]
        result[basic_unit] = {"up": up, "down": down, "left": left, "right": right}
    return result


def encode_ref_list(basic_units):
    result = {}
    for basic_unit in basic_units:
        up = basic_unit[:2]
        down = basic_unit[2:]
        left = basic_unit[0] + basic_unit[2]
        right = basic_unit[1] + basic_unit[3]
        result[up] = result.get(up, []) + [
            {"up": up, "down": down, "left": left, "right": right}
        ]
    return result


def init_set_of_previous(encoded_list):
    init_set_of_previous = {}
    for _, basic_unit in encoded_list.items():
        init_set_of_previous[basic_unit["down"]] = init_set_of_previous.get(
            basic_unit["down"], []
        ) + [{"left": basic_unit["left"], "right": basic_unit["right"]}]
    return init_set_of_previous


if __name__ == "__main__":
    print(encode_list_to_int(basic_unit_return_0))
    print(encode_list_to_int(basic_unit_return_1))
    print(encode_ref_list(basic_unit_return_0))
    print(encode_ref_list(basic_unit_return_1))
    print(init_set_of_previous(encode_list_to_int(basic_unit_return_0)))
    print(init_set_of_previous(encode_list_to_int(basic_unit_return_1)))
