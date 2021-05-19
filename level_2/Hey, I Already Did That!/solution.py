def solution(n,b):
    # Your code here
    cycle = [n]
    i = 0
    while i <1000:
        n = onestep(n,b)
        try:
            res = cycle.index(n)
            return len(cycle)-res
        except ValueError: 
            cycle.append(n)
        i += 1
    return "i>1000"

def numberToBase(n, b):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return ''.join(map(str,digits[::-1]))

def onestep(n,b):
    max_n = list(n)
    min_n =list(n)
    max_n.sort(reverse=True)
    min_n.sort()
    max_n = int("".join(max_n),b)
    min_n = int("".join(min_n),b)
    next_n = max_n - min_n
    return numberToBase(next_n,b)