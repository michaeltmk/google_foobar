from math import floor, sqrt

def solution(str_n):
    n = int(str_n)
    a = sqrt(2)
    return str(floor(sum_of_beatty(a,n)))

def sum_of_beatty(a,n):
    if n == 0:
        return 0
    if n == 1:
        return floor(a)
    if a >= 2:
        b = a-1
        print(f"{a=} {b=} {n=}")
        return sum_of_beatty(b,n) + n*(n+1)/2
    if a < 2 and a > 1:
        nd = floor((a-1)*n)
        b = 1/(1-(1/a))
        print(f"{a=} {b=} {n=} {nd=}")
        return (n+nd)*(n+nd+1)/2 - sum_of_beatty(b,nd)