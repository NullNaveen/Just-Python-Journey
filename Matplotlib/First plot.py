import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y)

# Add labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Show the plot
plt.show()


plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('Line Plot')

plt.subplot(1, 2, 2)
plt.bar('A', 'B', 'C'], [5, 7, 3])
plt.title('Bar Chart')

plt.show()

