def solution(x,y):
    # Your code here
    M = int(x)
    F = int(y)
    gen = 0
    while min(M,F) > 1:
        if max(M,F)%min(M,F) == 0:
            return "impossible"
        gen += max(M,F)//min(M,F)
        M,F = max(M,F)%min(M,F),min(M,F)

    if (M,F) == (1,1):
        return str(gen)
    else:
        gen += max(M,F)//min(M,F) -1
        return str(gen)
