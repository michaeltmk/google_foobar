import solution

def _test_solution():
    assert solution.solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) == 6
    assert solution.solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0] ]) == 16

def stupid_solution(entrances:list, exits:list, path:list):
    #delete the exit row, since no bunnies will return to rooms when it pass the exit
    for exit in exits:
        path.remove(exit)
    #start from entrances
    for entry in entrances:
        
def test_combine_multirow():
    assert solution.combine_multirow([[1,2,3],[1,2,3],[0,4,5]]) == [2,8,11]