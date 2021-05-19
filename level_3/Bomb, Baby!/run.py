import solution
import math
import random as r
print(solution.solution('2','1') == '1')
print(solution.solution('4','7') == '4')
print(solution.solution('4','2') == "impossible")
print(solution.solution('3','3') == "impossible")

for i in range(1):
    M = r.randint(0,(10**50))
    F = r.randint(0,(10**50))+1

    print('test on ',M,',',F)
    print(solution.solution(str(M),str(F)))
