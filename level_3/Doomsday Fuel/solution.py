import fractions

def find_LCM(denominators):
    common_denominator = 1
    terminal_states = []
    for idx, denominator in enumerate(denominators):
        if denominator == 0:
            denominators[idx] = 1
            terminal_states.append(idx)
            denominator = 1
        common_denominator = common_denominator*denominator/fractions.gcd(common_denominator, denominator)
    return common_denominator, denominators, terminal_states


def solution(m):
    # Your code here
    denominators = list(map(sum,m))
    common_denominator ,denominators, terminal_states = find_LCM(denominators)
    for idx, row in enumerate(m):
        if max(row) == 0:
            row[idx] = common_denominator
        else:
            m[idx] = list(map(lambda x: x*common_denominator/denominators[idx],row))
    # print('denominators',denominators)
    print('common_denominator',common_denominator)
    stochastic_matrix = m
    print('stochastic_matrix',stochastic_matrix)

    # print('eignvalue by np method')
    # eigenvalues, leigenvectors,reigenvectors  = scipy.linalg.eig(stochastic_matrix, left = True, right = True)
    # print(eigenvalues)
    # print(leigenvectors)
    # print(reigenvectors)
    # i = np.where(eigenvalues == common_denominator)[0]
    # eigenvectors = leigenvectors[:,-1]
    # print(eigenvectors)

    print('eignvalue by elimiation')
    general_equations = stochastic_matrix - common_denominator*np.identity(len(m))
    print(general_equations)
    for idx in terminal_states:
        LHS = np.copy(general_equations)
        del_states = terminal_states[:]
        del_states.remove(idx)
        LHS[idx,idx] = 1
        RHS = LHS[idx]
        # print(LHS)
        LHS = np.delete(LHS,del_states,axis = 0)
        LHS = np.delete(LHS,del_states,axis = 1)
        RHS = np.delete(RHS,del_states)
        print(LHS)
        print(RHS)
        X2 = np.linalg.solve(LHS,RHS)
        print('X2',X2)  
        # pl, u = lu(LHS, permute_l=True)
        # print('u',u)
        # p,l, u = lu(u)
        # print('l',l)


    # pl, u = lu(general_equations, permute_l=True)
    # print('u',u)

     
def float2int(list_):
    while min(List_) != 1:
        list_ = list(map(lambda x: x/min(list_),list_))
    

if __name__ == "__main__":
    print(find_LCM([3, 7, 1, 1, 1]))
    print(find_LCM([1.0, 0.0, -0.0, -0.21428571428571427, -0.14285714285714285, -0.6428571428571428]))
    
    # solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    # solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])