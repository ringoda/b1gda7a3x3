import numpy

#import the array from the .txt file
data = numpy.genfromtxt("array.txt", delimiter=",")

#extract all columns except the last one as matrix A
A = data[:,0:-1]

#extract the last column as b
b = data[:,-1]

#solve the linear matrix Ax=b
x = numpy.linalg.solve(A,b)

#print the result
print x