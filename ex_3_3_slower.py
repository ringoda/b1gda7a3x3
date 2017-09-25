#we use pythons time library to measure the run time
import time

#start time and below is endtime
#we simply run the cython code by importing
#the module we compiled from our .pyx file
#which we named ex_3_3
start1 = time.time()
import ex_3_3
end1 = time.time()

start = time.time()
#we want this done 500 times
for i in range(0,500):
	result = 0
	#the actual computation
	for k in range(1,10001):
		result = float(result) + 1/(float(k)**2)
#print the result from the last run, just done for confirmation
print 'Python result: ' + str(result)
end = time.time()

#print the runtimes which is found by subtracting end time from start time
print 'Python runtime: ' + str(end - start)
print 'Cython runtime: ' + str(end1 - start1)

