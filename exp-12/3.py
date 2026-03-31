import matplotlib.pyplot as plt
x=['a','b','c','d']
y=[3,7,5,9]
# plt.plot(x,y)
plt.title('Bar Plot')
plt.bar(x,y,color='g',label='Bar Data')
plt.xlabel("x_axis")
plt.ylabel('y_axis')
plt.legend()
# plt.grid()
plt.show()