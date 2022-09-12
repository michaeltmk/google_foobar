from re import A
import solution
import random
from math import sqrt, floor


def test_solution():
    assert solution.solution('77') == "4208"
    assert solution.solution('5') == "19"
    
def test_sum_of_beatty():
    assert solution.sum_of_beatty(sqrt(2) , 77) == 4208
    assert solution.sum_of_beatty(sqrt(2), 5) == 19
    assert solution.sum_of_beatty(sqrt(2), 0) == 0
    for Q in range(2,5):
        print(Q)
        assert solution.sum_of_beatty(sqrt(Q), 1) == floor(sqrt(Q)) , f"{Q=}"

if __name__ == '__main__':
    test_solution()
    for _ in range(100):
        print(solution.solution(str(random.randint(1,10000000000000000000000000))))