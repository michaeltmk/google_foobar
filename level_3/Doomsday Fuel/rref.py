def ToReducedRowEchelonForm( M):
    if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        print('lead',lead)
        print('lv',lv)
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
        
        
    
 
mtx = [
   [-18,9,0,0,0,9],
   [8,-18,0,6,4,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],
   [0,0,0,0,0,0],]
 
ToReducedRowEchelonForm( mtx )
 
for idx ,rw in enumerate(mtx):
    mtx[idx] = list(map(lambda x: x, rw))
#   print(', '.join((str(rv) for rv in rw)))
# print(int(mtx[0][-1]))
print(mtx)