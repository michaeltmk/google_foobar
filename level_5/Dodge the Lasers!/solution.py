from decimal import Decimal, localcontext

def solution(str_n):
    n = int(str_n)
    with localcontext() as ctx:
        ctx.prec = 102
        a = Decimal(2).sqrt()
        return str(int(sum_of_beatty(a,n)))

def sum_of_beatty(a,n):
    if n == 0:
        return 0
    m = int(a*n)
    nd = int((a-1)*n)
    return (m*(m+1))/2 - sum_of_beatty(a,nd)  - nd*(nd+1)