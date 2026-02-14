#Solution
#Multiply of two matrices

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
b = [[1,2,3],
     [4,2,1],
     [4,2,4]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]     
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += b[i][k]*b[k][j]
for result in result:
    print(result)
