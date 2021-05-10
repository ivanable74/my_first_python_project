#Магическая спираль
size_matrix=int(input())
s = 0

matrix = [[] for I in range(size_matrix)]
for i in range(size_matrix):
    for j in range(size_matrix):
        matrix[i].append(0)

for t in range(1,size_matrix+1):
    for i in range(t-1,size_matrix-t+1):
        s+=1
        matrix[t-1][i] = s
    for i in range(t,size_matrix-t+1):
        s+=1
        matrix[i][size_matrix-t] = s
    for i in reversed(range(t-1,size_matrix-t)):
        s+=1
        matrix[size_matrix-t][i] = s
    for i in reversed(range(t,size_matrix-t)):
        s+=1
        matrix[i][t-1] = s


for i in range(size_matrix):
    for j in range(size_matrix):
        print(matrix[i][j],end=' ')
    print("\n",end="") 