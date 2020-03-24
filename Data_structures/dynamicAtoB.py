


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