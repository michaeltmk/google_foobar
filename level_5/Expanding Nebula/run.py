import solution
import random


def test_set_of_previous_1d():
    assert solution.set_of_previous_1d(
        [0, 1], solution.encoded_list_0_, solution.encoded_list_1_
    ) == [
        {"left": "0001", "right": "0000"},
        {"left": "1001", "right": "1000"},
        {"left": "0000", "right": "0001"},
        {"left": "1000", "right": "1001"},
        {"left": "1110", "right": "0000"},
        {"left": "0110", "right": "1000"},
        {"left": "1110", "right": "1000"},
        {"left": "1000", "right": "0110"},
        {"left": "0000", "right": "1110"},
        {"left": "1000", "right": "1110"},
    ]


def test_solution():
    assert (
        solution.solution(
            [
                [True, True, False, True, False, True, False, True, True, False],
                [True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, False, False, False, True],
                [False, True, False, False, False, False, True, True, False, False],
            ]
        )
        == 11567
    )
    assert (
        solution.solution(
            [[True, False, True], [False, True, False], [True, False, True]]
        )
        == 4
    )
    assert (
        solution.solution(
            [
                [True, False, True, False, False, True, True, True],
                [True, False, True, False, False, False, True, False],
                [True, True, True, False, False, False, True, False],
                [True, False, True, False, False, False, True, False],
                [True, False, True, False, False, True, True, True],
            ]
        )
        == 254
    )


def test_dynamic_filling():
    past = {"1000": 10, "0100": 20, "0010": 30, "0001": 40}
    next_ref = {"1000": ["1000", "0011"], "0100": ["1001", "0011"]}
    assert solution.dynamic_filling(past, next_ref) == {
        "1000": 10,
        "1001": 20,
        "0011": 30,
    }


def test_multi_decode():
    assert solution.multi_decode(
        [
            {"left": "10000000", "right": "00000000"},
            {"left": "10010110", "right": "00010100"},
            {"left": "10010110", "right": "00010101"},
        ]
    ) == {"10000000": ["00000000"], "10010110": ["00010100", "00010101"]}


def _test_case_gener():
    q_grid_i = random.randint(3, 9)
    q_grid_j = random.randint(3, 50)
    grid = []
    for i in range(q_grid_i):
        grid.append([])
        for j in range(q_grid_j):
            grid[i].append(random.choice([True, False]))
    ground_truth = solution.solution(grid)
    return grid, ground_truth


def test_filling():
    encoded_list_0 = solution.encoded_list_0_
    encoded_list_1 = solution.encoded_list_1_
    assert (
        solution.filling([], 1, encoded_list_0, encoded_list_1)
        == solution.init_set_of_previous_1
    )
    assert (
        solution.filling([], 0, encoded_list_0, encoded_list_1)
        == solution.init_set_of_previous_0
    )
    assert solution.filling(
        solution.init_set_of_previous_1,
        0,
        encoded_list_0,
        encoded_list_1,
    ) == {
        "00": [{"left": "1000", "right": "0000"}, {"left": "0000", "right": "1000"}],
        "11": [
            {"left": "1001", "right": "0001"},
            {"left": "0001", "right": "1001"},
            {"left": "0111", "right": "0001"},
            {"left": "0001", "right": "0111"},
        ],
        "10": [{"left": "0111", "right": "0000"}, {"left": "0001", "right": "0110"}],
        "01": [{"left": "0110", "right": "0001"}, {"left": "0000", "right": "0111"}],
    }


def _test_solution2():
    assert (
        solution.solution2(
            [
                [True, True, False, True, False, True, False, True, True, False],
                [True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, False, False, False, True],
                [False, True, False, False, False, False, True, True, False, False],
            ]
        )
        == 11567
    )
    assert (
        solution.solution2(
            [[True, False, True], [False, True, False], [True, False, True]]
        )
        == 4
    )
    assert (
        solution.solution2(
            [
                [True, False, True, False, False, True, True, True],
                [True, False, True, False, False, False, True, False],
                [True, True, True, False, False, False, True, False],
                [True, False, True, False, False, False, True, False],
                [True, False, True, False, False, True, True, True],
            ]
        )
        == 254
    )


def _test_compare_solution():
    for _ in range(100):
        grid, ground_truth = _test_case_gener()
        assert solution.solution2(grid) == ground_truth


if __name__ == "__main__":
    # _test_solution()
    # _test_encode_list_to_int()
    # test_filling()
    print(solution.encoded_list_0_)
    print(solution.encoded_list_1_)
