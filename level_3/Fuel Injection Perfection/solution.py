def operation(n):
    if n%2==0:
        n = n/2
    elif n==3 or n%4==1: #the significant bits are 011 / 01
        n -= 1
    else: #the significant bits are 111
        n += 1
    return n

def solution(fuel): 
    '''
    when you use binary to represent the number, 0 means it is divised by 2, 1 means it is subtract 1 then devised by 2.
    In order to minimise the steps, for any 3 significant bits are 111, it should add 1 then divided by 2.
    '''       
    fuel = int(fuel)
    r = 0
    while fuel >1:
        fuel = operation(fuel)
        r+=1
    return r