import matplotlib.pyplot as plt
data=[2,5,6,7,8,9,10,1,4,14]

# plt.plot(x,y)
plt.hist(data,bins=5,color='purple')
plt.title('Histogram')
label='Histogram data'
plt.boxplot(data)
plt.xlabel("Bins")
plt.ylabel('Frequency')
plt.legend()
plt.show()