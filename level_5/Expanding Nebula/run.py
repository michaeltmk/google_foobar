import solution

def _test_solution():
    assert solution.solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]) == 11567
    assert solution.solution([[True, False, True], [False, True, False], [True, False, True]]) == 4
    assert solution.solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]) == 254

def _test_encode_list_to_int():
    print(solution.encode_list_to_int())

def test_filling():
    encoded_list_0 = solution.encode_list_to_int(solution.basic_unit_return_0)
    encoded_list_1 = solution.encode_list_to_int(solution.basic_unit_return_1)
    assert solution.filling([],1,encoded_list_0, encoded_list_1) == [[encoded_list_1[k]] for k in encoded_list_1.keys()]
    assert solution.filling([],0,encoded_list_0, encoded_list_1) == [[encoded_list_0[k]] for k in encoded_list_0.keys()]
    assert solution.filling(
            [[encoded_list_1[k]] for k in encoded_list_1.keys()], 
            0,
            encoded_list_0, 
            encoded_list_1
        ) == \
        [
            [{'up': '10', 'down': '00', 'left': '10', 'right': '00'}, {'up': '00', 'down': '00', 'left': '00', 'right': '00'}], 
            [{'up': '10', 'down': '00', 'left': '10', 'right': '00'}, {'up': '00', 'down': '11', 'left': '01', 'right': '01'}], 
            [{'up': '01', 'down': '00', 'left': '00', 'right': '10'}, {'up': '00', 'down': '00', 'left': '00', 'right': '00'}], 
            [{'up': '01', 'down': '00', 'left': '00', 'right': '10'}, {'up': '00', 'down': '11', 'left': '01', 'right': '01'}], 
            [{'up': '00', 'down': '10', 'left': '01', 'right': '00'}, {'up': '10', 'down': '10', 'left': '11', 'right': '00'}], 
            [{'up': '00', 'down': '10', 'left': '01', 'right': '00'}, {'up': '10', 'down': '01', 'left': '10', 'right': '01'}], 
            [{'up': '00', 'down': '10', 'left': '01', 'right': '00'}, {'up': '10', 'down': '11', 'left': '11', 'right': '01'}], 
            [{'up': '00', 'down': '01', 'left': '00', 'right': '01'}, {'up': '01', 'down': '10', 'left': '01', 'right': '10'}], 
            [{'up': '00', 'down': '01', 'left': '00', 'right': '01'}, {'up': '01', 'down': '01', 'left': '00', 'right': '11'}], 
            [{'up': '00', 'down': '01', 'left': '00', 'right': '01'}, {'up': '01', 'down': '11', 'left': '01', 'right': '11'}]
        ]

def test_multi_decode():
    assert solution.multi_decode(
            [
                [{'up': '10', 'down': '00', 'left': '10', 'right': '00'}, {'up': '00', 'down': '00', 'left': '00', 'right': '00'}], 
                [{'up': '10', 'down': '00', 'left': '10', 'right': '00'}, {'up': '00', 'down': '11', 'left': '01', 'right': '01'}]
            ]
        ) == \
                [
                    {'left': '1000', 'right': "0000"},
                    {'left': '1001', 'right': '0001'}
                ]

def test_set_of_previous_1d():
    assert \
        solution.set_of_previous_1d([0,1],solution.encoded_list_0,solution.encoded_list_1) == \
        [
            {'left': '0001', 'right': '0000'}, 
            {'left': '0000', 'right': '0001'},
            {'left': '1001', 'right': '1000'}, 
            {'left': '1000', 'right': '1001'}, 
            {'left': '1110', 'right': '0000'}, 
            {'left': '1000', 'right': '0110'}, 
            {'left': '0110', 'right': '1000'}, 
            {'left': '0000', 'right': '1110'}, 
            {'left': '1110', 'right': '1000'}, 
            {'left': '1000', 'right': '1110'}
        ]



if __name__ == '__main__':
    # _test_solution()
    # _test_encode_list_to_int()
    test_filling()