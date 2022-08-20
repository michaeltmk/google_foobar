import solution
import random 

def stupid_isInfiniteLoop(a,b):
    number_of_loop = 0
    history_a = []
    while a!=b and (a not in history_a or number_of_loop == 0):
        history_a.append(a)
        if a > b:
            a = a-b
            b = 2*b
        else:
            b = b-a
            a = 2*a
        number_of_loop += 1
        # print(f'{number_of_loop=}, {a=}, {b=} ')
    if a == b:
        return False
    else:
        return True

def isInfiniteLoop2(a,b):
    na = 0
    nb = 0
    while a%2 == 0:
        na += 1
        a = a/2
    while b%2 == 0:
        nb += 1
        b = b/2
    if na != nb:
        return True
    else:
        return solution.isInfiniteLoop(a,b)

def use_matrix_alone(banana_list):
    result = solution.use_matrix(banana_list)
    return result if len(banana_list)%2 == 0 else result+1

def test_solution():
    assert solution.solution([1,1]) == 2
    assert solution.solution([1, 7, 3, 21, 13, 19]) == 0
    assert solution.solution([1, 7, 3, 21, 13, 19,2]) == 1
    assert use_matrix_alone([1, 7, 3, 21, 13, 19,2]) == 1
    #random check
    for i in range(100000):
        banana_list = [random.randint(1,1073741823) for _ in range(random.randint(1,100))]
        print(f'banana_list: {banana_list}')
        assert solution.solution(banana_list) == use_matrix_alone(banana_list)
    
def _test_isInfiniteLoop2():
    for i in range(1000):
        a = random.randint(1,100)
        b = random.randint(1,100)
        assert isInfiniteLoop2(a,b) == solution.isInfiniteLoop(a,b)
        print(f"{a} {b}")
        print(f"{isInfiniteLoop2(a,b)} {solution.isInfiniteLoop(a,b)}")
        print("")

def _test_isInfiniteLoop():
    assert solution.isInfiniteLoop(1,1)==False
    assert solution.isInfiniteLoop(1,2)==True
    assert solution.isInfiniteLoop(9,1)==True
    assert solution.isInfiniteLoop(8,2)==True
    assert solution.isInfiniteLoop(6,4)==True

    assert solution.isInfiniteLoop(4,2)==True
    assert solution.isInfiniteLoop(5,1)==True

    assert solution.isInfiniteLoop(4,1)==True
    assert solution.isInfiniteLoop(2,3)==True


    assert solution.isInfiniteLoop(1,15)==False
    assert solution.isInfiniteLoop(2,14)==False
    assert solution.isInfiniteLoop(3,13)==False
    assert solution.isInfiniteLoop(4,12)==False
    assert solution.isInfiniteLoop(5,11)==False
    assert solution.isInfiniteLoop(6,10)==False
    assert solution.isInfiniteLoop(7,9)==False
    assert solution.isInfiniteLoop(8,8)==False

    assert solution.isInfiniteLoop(1,19)==True
    assert solution.isInfiniteLoop(2,18)==True
    assert solution.isInfiniteLoop(3,17)==True
    assert solution.isInfiniteLoop(4,16)==True
    assert solution.isInfiniteLoop(5,15)==False
    assert solution.isInfiniteLoop(6,14)==True
    assert solution.isInfiniteLoop(7,13)==True
    assert solution.isInfiniteLoop(8,12)==True
    assert solution.isInfiniteLoop(9,11)==True
    assert solution.isInfiniteLoop(10,10)==False
    assert solution.isInfiniteLoop(11,9)==True
    assert solution.isInfiniteLoop(12,8)==True

    assert solution.isInfiniteLoop(1,23)==True
    assert solution.isInfiniteLoop(2,22)==True
    assert solution.isInfiniteLoop(3,21)==False
    assert solution.isInfiniteLoop(4,20)==True
    assert solution.isInfiniteLoop(5,19)==True
    assert solution.isInfiniteLoop(6,18)==False
    assert solution.isInfiniteLoop(7,17)==True
    assert solution.isInfiniteLoop(8,16)==True
    assert solution.isInfiniteLoop(9,15)==False
    assert solution.isInfiniteLoop(10,14)==True
    assert solution.isInfiniteLoop(11,13)==True
    assert solution.isInfiniteLoop(12,12)==False
    assert solution.isInfiniteLoop(13,11)==True

    assert solution.isInfiniteLoop(1,29)==True
    assert solution.isInfiniteLoop(2,28)==True
    assert solution.isInfiniteLoop(3,27)==True
    assert solution.isInfiniteLoop(4,26)==True
    assert solution.isInfiniteLoop(5,25)==True
    assert solution.isInfiniteLoop(6,24)==True
    assert solution.isInfiniteLoop(7,23)==True
    assert solution.isInfiniteLoop(8,22)==True
    assert solution.isInfiniteLoop(9,21)==True
    assert solution.isInfiniteLoop(10,20)==True
    assert solution.isInfiniteLoop(11,19)==True
    assert solution.isInfiniteLoop(12,18)==True
    assert solution.isInfiniteLoop(13,17)==True
    assert solution.isInfiniteLoop(14,16)==True
    assert solution.isInfiniteLoop(15,15)==False

def test_time_isInfiniteLoop():
    for i in range(1):
        a = 751586883
        b = 767373791
        print(f"{a=}, {b=}")
        print(f"{solution.isInfiniteLoop(a,b)}")
        print("")
    assert solution.isInfiniteLoop(83,10) == True

def test_time_stupid_isInfiniteLoop():
    for i in range(1):
        a = 751586883
        b = 767373791
        print(f"{a=}, {b=}")
        print(f"{stupid_isInfiniteLoop(a,b)}")
        print("")
    assert stupid_isInfiniteLoop(83,10) == True
    
def _test_manual_isInfiniteLoop():
    for i in range(100):
        a = random.randint(1,1073741823)
        b = random.randint(1,1073741823)
        print(f"{a=}, {b=}")
        assert stupid_isInfiniteLoop(a,b)== solution.isInfiniteLoop(a,b)
        # print(stupid_isInfiniteLoop(a,b))
        # print(f"{solution.isInfiniteLoop(a,b)}")
if __name__ == '__main__':
    # test_solution()
    _test_manual_isInfiniteLoop()
    test_time_isInfiniteLoop()    
    test_time_stupid_isInfiniteLoop()
    print("All tests passed")