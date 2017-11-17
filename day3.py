import statistics as stat

li = [4,4,6,4,2,6,11,7,12,8]

Mean=stat.mean(li)
Median=stat.median(li)
Mode=stat.mode(li)
StandDev=stat.stdev(li)
Variance=stat.variance(li)

print(Mean)
print(Median)
print(Mode)
print(StandDev)
print(Variance)

#Draw Line
import matplotlib.pyplot as plt
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.plot([1,2,3],[5,7,4])
plt.show()


#Two Line in Single Graph
x1=[1,2,3]
y1=[2,5,3]
x2=[4,2,5]
y2=[1,7,3]

plt.plot(x1,y1,label="First Line",color="Violet")
plt.plot(x2,y2,label="Second Line",color="yellow")
plt.legend()
plt.show()

#Bar Chart
x1=[1,3,5,4,2,5]
y2=[8,2,6,4,2,5]
plt.bar(x1,y2,label="Bar chart",color="Green")
plt.show()

#histogram
population=[12,13,23,53,13,13,53, 6, 4, 7,69,3 ,25,87,24,23,77]
beans=[00,10,20,30,40,50,60,70,80]
plt.hist(population,beans,histtype="bar",rwidth=0.4)
plt.legend()
plt.show()

#Scatter plot of points
x1=[1,3,5,4,2,5]
y1=[8,2,6,4,2,5]
plt.scatter(x1,y1,marker="o",s=50,)
plt.legend()
plt.show()
