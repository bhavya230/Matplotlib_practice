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

plt.scatter(x,y,c="g",label="data points")
plt.xlabel('x axis') # lael for x axis 
plt.ylabel('y axis') # label for y axis
plt.title('Graph in 2D') # gives title to graph
plt.legend() 
plt.savefig("Test.png") # to save the image directly 
plt.show() # show the graph

# plt plot -- line graph
x1=np.arange(1,11)
y1=np.arange(11,21)
y2=np.arange(21,31)

plt.plot(x1,y1,marker="o",color="red",linestyle="--",markerfacecolor="red",label=" red data")
plt.plot(x1,y2,marker="*",color="green",linestyle="-",markerfacecolor="green",label=" green data")
plt.legend()
plt.grid(True)
plt.xlabel("x axis")
plt.ylabel("y label")
plt.title("Multiplt Line Graph")
plt.show()

# creating subplots
plt.subplot(1,2,1)
plt.plot(x1,y1)
plt.xlabel("x axis")
plt.ylabel(" y axix")
plt.title("line graph")

plt.subplot(1,2,2)
plt.bar(x1,y2)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("bar graph")

plt.tight_layout()
plt.show()