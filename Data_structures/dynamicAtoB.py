


def AtoB():

    m = n= 3

    mat = list([0]*n for i in range(m))

    for i in range(m):

        for j in range(n):

            if i == 0 or j ==0:
                mat[i][j] = 1
            
            else:
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
    
    return mat[m-1][n-1]


print(AtoB())


def AtoBObstacles(tracemat):

    m=n  = len(tracemat)
    

    mat = list([0]*n for i in range(m))

    for i in range(m):

        for j in range(n):

            if i ==0 and j==0 and tracemat[i][j] != 1:
                mat[i][j] = 1
            
            elif tracemat[i][j] == 1:
                mat[i][j] =0
            
            elif i ==0 and tracemat[i][j] !=1:
                mat[i][j] = mat[i][j-1]
            
            elif j == 0 and tracemat[i][j] !=1:
                mat[i][j] = mat[i-1][j]
            
            else:
                mat[i][j] = mat[i][j-1] + mat[i-1][j]
    
    return mat

            

tracemat = [[0,0,0],[0,1,0],[0,0,0]]
tracemat = [[1,0],[0,0]]
tracemat = [[0,1],[1,0]]
AtoBObstacles(tracemat)
            


