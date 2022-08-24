import solution

def test_solution():
    assert solution.solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) == 6
    assert solution.solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0] ]) == 16

def test_find_path():
    assert solution.find_path(0, 3, [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) == ([0,1,2,3],6)
    assert solution.find_path(0, 3, [[0, 7, 0, 5], [0, 0, 6, 1], [0, 0, 0, 8], [9, 0, 0, 0]]) == ([0,1,2,3],6)
    assert solution.find_path(0, 3, [[0, 7, 0, 5], [0, 0, 0, 1], [0, 0, 0, 8], [9, 0, 0, 0]]) == ([0,1,3],1)
    assert solution.find_path(0, 3, [[0, 7, 0, 5], [0, 0, 0, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) == ([0,3],5)

def test_find_all_paths():
    assert solution.find_all_paths([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) == [([0,1,2,3],6)]
    assert solution.find_all_paths([0], [3], [[0, 7, 0, 5], [0, 0, 6, 1], [0, 0, 0, 8], [9, 0, 0, 0]]) == [([0,1,2,3],6),([0,1,3],1),([0,3],5)]