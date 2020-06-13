import time
import threading
#Define function to multiply matrix
def multiply_Matrix_Child(i, X, Y):
	# iterate through columns of Y
	for j in range(len(Y[0])):
		# iterate through rows of Y
		for k in range(len(Y)):
			#print(i,j,k)
			result[i][j] += X[i][k] * Y[k][j]
def job(i, X, Y):
	for k in range(7*i, 7*(i+1)):
		multiply_Matrix_Child(k, X, Y)
def multiply_Matrix(X, Y):
	for t in range(0, int(len(X)/7)):
		# Create a child thread
		ct = threading.Thread(target = job(t, X, Y))
		# Execute the thread
		ct.start()
	ct.join()
#Generate martix A
column, row = 35, 60
matA = [[0 for _ in range(row)] for _ in range(column)]
for i in range(column):
	for j in range(row):
		matA[i][j]=3.5*(i+1)-6.6*(j+1)
#Generate martix B
column, row = 60, 35
matB = [[0 for _ in range(row)] for _ in range(column)]
for i in range(column):
	for j in range(row):
		matB[i][j]=6.6+8.8*(i+1)-3.5*(j+1)
#Generate martix C (zero matrix)
column, row = 35, 35
matC = [[0 for _ in range(row)] for _ in range(column)]
result = [[0 for _ in range(len(matA))] for _ in range(len(matB[0]))]
startTime = time.time()
multiply_Matrix(matA, matB)
stopTime = time.time()
print('execute time:',round((stopTime-startTime)*1000),'ms')

