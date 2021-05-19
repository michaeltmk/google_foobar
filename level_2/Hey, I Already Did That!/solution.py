def solution(s):
    # Your code here
    idx = 0
    num_of_employee = 0
    salutes = []
    while idx<len(s):
        if s[idx] == ">" or s[idx] == "<":
            num_of_employee += 1
            if s[idx] == "<":
                salutes.append(num_of_employee -1-len(salutes))
        idx += 1
    return sum(salutes)*2