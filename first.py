import matplotlib
import numpy as np

# importing pyplot submodule of matplotlib-- that contains most of its utilities 

import matplotlib.pyplot as plt

# checking version of matplotlib
print(matplotlib.__version__)

# 1 example
x=np.arange(0,10)
y=np.arange(11,21)

a=np.arange(40,50)
b=np.arange(50,60)

# plotting using matplotlib

# plt scatter plot

plt.scatter(x,y,c="g")
plt.xlabel('x axis') # lael for x axis 
plt.ylabel('y axis') # label for y axis
plt.title('Graph in 2D') # gives title to graph 
plt.show() # show the graph
plt.savefig("Test.png") # to save the image directly 