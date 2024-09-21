from sys import argv
 
def main():
    n = int(argv[1])
    A, b = buildMatrices(n)
    print("Populacao para", n, "salas:", sum(thomas(A, b, n)), "atores")

def buildMatrices(n):
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        if i == 0:
            A[i][i] = (n-1)/(2*n) - 1
            A[i][i+1] = 1/2
        elif i == n-1:
            A[i][i-1] = 1/2
            A[i][i] = (n-1)/(2*n) - 1
        else:
            A[i][i-1] = 1/2
            A[i][i] = -1
            A[i][i+1] = 1/2

    b = [0] * n
    b[(((n+1)//2)-1)] = -1
    
    return A, b

def thomas(A, b, n):
    c = [0] * (n-1)
    d = [0] * n

    d = forwardSub(A, b, c, d, n)

    return backSub(c, d, n)

def forwardSub(A, b, c, d, n):
    c[0] = A[0][1] / A[0][0]
    d[0] = b[0] / A[0][0]

    for i in range(1, n-1):
        aux = A[i][i] - A[i][i-1] * c[i-1]
        c[i] = A[i][i+1] / aux
        d[i] = (b[i] - A[i][i-1] * d[i-1]) / aux
    
    d[n-1] = (b[n-1] - A[n-1][n-2] * d[n-2]) / (A[n-1][n-1] - A[n-1][n-2] * c[n-2])
    
    return d

def backSub(c, d, n):
    for i in range(n-2, -1, -1):
        d[i] = d[i] - c[i] * d[i+1]    
    
    return d 


main()