import time
# import numpy as np
#Define function to transpose matrix
def transpose_Matrix(m):
	r = [[] for i in m[0]]
	for ele in m:
		for i in range(len(ele)):
			r[i].append(ele[i])
	return r
#Define function to multiply matrix
def multiply_Matrix(X, Y):
	#print(len(X), len(Y[0]))
	result = [[0 for _ in range(len(X))] for _ in range(len(Y[0]))]
	for i in range(len(X)):
		# iterate through columns of Y
		for j in range(len(Y[0])):
			# iterate through rows of Y
			for k in range(len(Y)):
				#print(i,j,k)
				result[i][j] += X[i][k] * Y[k][j]
	return result
#Generate martix A
column, row = 350, 600
matA = [[0 for _ in range(row)] for _ in range(column)]
for i in range(column):
	for j in range(row):
		matA[i][j]=3.5*(i+1)-6.6*(j+1)
#Generate martix B
column, row = 600, 350
matB = [[0 for _ in range(row)] for _ in range(column)]
for i in range(column):
	for j in range(row):
		matB[i][j]=6.6+8.8*(i+1)-3.5*(j+1)
#Generate martix C (zero matrix)
column, row = 350, 350
matC = [[0 for _ in range(row)] for _ in range(column)]
startTime = time.time()
matC = multiply_Matrix(matA, matB)
stopTime = time.time()
print(matC)
#---------------------------------
##List to np.array
# print(len(matC[0]),len(matC))
# matC = np.multiply(matA, transpose_Matrix(matB))
# npMatC = np.asarray(matC)
# print(npMatC)
#---------------------------------
print('execute time:',round((stopTime-startTime)*1000),'ms')