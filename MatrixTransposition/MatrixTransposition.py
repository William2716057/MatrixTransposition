
#transposes matrix in A so horizontal columns will be displayed vertically
A = [[5,4,3],
    [2,4,6],
    [4,7,9],
    [8,1,4]]

#empty matrix of reverse order
TranspositionResult = [[0,0,0,0],
                 [0,0,0,0],
                 [0,0,0,0]]

#Iterate over rows of original matrix 
for a in range(len(A)):
    #iterate over columns of original matrix 
    for b in range(len(A[0])):
        #stores value [a] in [b] and value [b] in [a]
        TranspositionResult[b][a] = A[a][b] # a = current row, b = current column

print("Matrix A Transposition: ")
for result in TranspositionResult:
    print(result)