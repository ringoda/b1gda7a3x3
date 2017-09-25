import numpy as np
from scipy import interpolate, optimize
import matplotlib.pyplot as plt

#import the points from the .txt file
data = np.genfromtxt('points.txt')

x = data[:,0]  #first column
y = data[:,1]  #second column

#interpolate the points
f = interpolate.interp1d(x, y)

#create the points for the interpolation
xnew = np.arange(-20,19,0.5)
#use interpolation function returned by 'interp1d'
ynew = f(xnew)

#find the real root using one of scipy's optimize functions 
root_value = optimize.root(f, 0, method='lm')

#create a plot figure
fig = plt.figure()
#add a plot for the figure, '111' means the layout of the plots should be a 1x1 array
#and the following plot is the first plot (and the only one in or case)
ax1 = fig.add_subplot(111)

#add title to the plot
ax1.set_title("Points X & Y")
#add label to x & y axis    
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

#plot the points, 'c' param is for specifying color (red in this case)
ax1.plot(x,y, c='r', label='the data')

#plot the interpolation points and mark them with 'x'
ax1.plot(xnew, ynew, 'x', label='the interpolation')

#plot the root value and mark it with 'o', the root value
#is in root_value.x which is an array an we get the first (and only) element
#the y-value for the root is of course 0
ax1.plot(root_value.x[0], 0, 'o', label='root')

#add the legend to the plot for clarification
leg = ax1.legend()

#actually show the plot
plt.show()