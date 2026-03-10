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
plt.savefig("LineGraph.png")
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
plt.savefig("Subplot.png")
plt.show()

# SINE GRAPH
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.title("Sine Graph")
plt.savefig("Sine.png")
plt.show()

# sine cosine graph on subplots
x=np.arange(0, 5*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)

plt.subplot(2,1,1)
plt.title("sine graph")
plt.plot(x,y_sin,color="red")

plt.subplot(2,1,2)
plt.title(" cosine graph")
plt.plot(x,y_cos,color="blue")

plt.tight_layout()
plt.savefig("SineCosine.png")
plt.show()

#Bar plot
subjects=["physics","chemistry","maths","english","computer science"]
marks=[83,95,95,95,89]

plt.bar(subjects,marks,color="green",width=0.5,align="center")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.title("bar graph")
plt.grid(True)
plt.savefig("bar.png")
plt.show()

# histograms
a=np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a)
plt.title("histogram")
plt.savefig("histogram.png")
plt.show()

# boxplot
data=[np.random.normal(0,std,100) for std in range(1,4)]

plt.boxplot(data,vert=True,patch_artist=True)
plt.savefig("boxplot.png")
plt.show()

# pie charts 
values=[215,130,245,210]
lables=['python','c++','ruby','java']

plt.pie(values,labels=lables,explode=[0.2,0.0,0.0,0.0],autopct='%1.1f%%',shadow=True)
plt.legend()
plt.title("pie chart")
plt.axis('equal')
plt.savefig('pieChart.png')
plt.show()