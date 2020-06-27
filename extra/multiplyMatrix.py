import time
def transpose_Matrix(m):
	r = [[] for i in m[0]]
	for ele in m:
		for i in range(len(ele)):
			r[i].append(ele[i])
	return r
def multiply_Matrix(X, Y):
	result = [[0 for _ in range(len(X))] for _ in range(len(Y[0]))]
	for i in range(len(X)):
		for j in range(len(Y[0])):
			for k in range(len(Y)):
				result[i][j] += X[i][k] * Y[k][j]
	return result
column, row = 350, 600
matA = [[0 for _ in range(row)] for _ in range(column)]
for i in range(column):
	for j in range(row):
		matA[i][j]=3.5*(i+1)-6.6*(j+1)
column, row = 600, 350
matB = [[0 for _ in range(row)] for _ in range(column)]
for i in range(column):
	for j in range(row):
		matB[i][j]=6.6+8.8*(i+1)-3.5*(j+1)
column, row = 350, 350
matC = [[0 for _ in range(row)] for _ in range(column)]
startTime = time.time()
matC = multiply_Matrix(matA, matB)
stopTime = time.time()
print('execute time:',round((stopTime-startTime)*1000),'ms')