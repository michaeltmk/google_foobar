import solution
import random
from math import sqrt, floor
from decimal import Decimal

def test_solution():
    assert solution.solution('77') == "4208"
    assert solution.solution('5') == "19"
    
def test_sum_of_beatty():
    assert solution.sum_of_beatty(Decimal(2).sqrt() , Decimal(77)) == 4208
    assert solution.sum_of_beatty(Decimal(2).sqrt(), Decimal(5)) == 19
    assert solution.sum_of_beatty(Decimal(2).sqrt(), Decimal(0)) == 0
    for Q in range(2,5):
        print(Q)
        assert solution.sum_of_beatty(sqrt(Q), 1) == floor(sqrt(Q)) , f"{Q=}"

def _test_speed():
    for i in range(100):
        n = Decimal(random.randint(10*90,10**100))
        assert solution.solution(str(n)) == str(int(solution.sum_of_beatty(Decimal(2).sqrt(),n)))

if __name__ == '__main__':
    test_solution()
    # for _ in range(100):
    #     print(solution.solution(str(random.randint(10**99,10**100))))
    for i in range(100):
        print(solution.solution(str(i)))