def solution(x,y):
    # Your code here
    M = int(x)
    F = int(y)
    gen = 0
    while M>0 and F>0:
        if M %2 == 0 and F%2 == 0:
            return "impossible"
        if F == 1 and M == 1:
            print("gen :",gen," (",M, "," ,F,")" )
            return str(gen)
        elif M>F:
            M = M-F
            gen += 1
            print("gen :",gen," (",M, "," ,F,")" )
        else:
            F = F-M
            gen += 1
            print("gen :",gen," (",M, "," ,F,")" )
    print("gen :",gen," (",M, "," ,F,")" )
    return "impossible"