from decimal import Decimal, getcontext
from math import floor

getcontext().prec = 101
root2 = Decimal(2).sqrt()
states = (root2,root2+1,root2+2)
root2_minus1 = states[0]-1

def solution(str_n):
    n = Decimal(str_n)
    a = states[0]
    return str(int(sum_of_beatty(a,n)))

def sum_of_beatty(a,n):
    if n == 0:
        return 0
    if n == 1:
        return floor(a)
    nd = floor(root2_minus1*n)
    nd = Decimal(nd)
    b = states[-1]
    if a == states[-1]:
        return (n+nd)*(n+nd+1)/2 + n*(n+1) - sum_of_beatty(b,nd)
    elif a == states[0]:
        return (n+nd)*(n+nd+1)/2 - sum_of_beatty(b,nd)