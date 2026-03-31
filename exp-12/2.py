import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
# plt.plot(x,y)
plt.title('Scatter points')
plt.scatter(x,y,linestyle='--',color='b',label='Scatter points')
plt.xlabel("x_axis")
plt.ylabel('y_axis')
plt.legend()
plt.grid()
plt.show()