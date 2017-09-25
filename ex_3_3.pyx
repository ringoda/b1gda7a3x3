#declare variables specifying type
cdef int k,i
cdef float result

#we want this done 500 times
for i in range(0,500):
	result = 0
	#the actual computation
	for k in range(1,10001):
		result = float(result) + 1/(float(k)**2)
#print the result from the last run, just done for confirmation
print 'Cython result: ' + str(result)
