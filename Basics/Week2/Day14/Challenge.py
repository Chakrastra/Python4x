import matplotlib.pyplot as plt

# Sample data
x = range(10)
y1 = [i for i in x]
y2 = [i**2 for i in x]

#line plot
plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='y = x')  # Line plot for y = x
plt.plot(x, y2, label='y = x^2')  # Line plot for y = x^2
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.legend()
plt.grid(True)
plt.show()

#scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(x, y1, label='y = x')  # Scatter plot for y = x
plt.scatter(x, y2, label='y = x^2')  # Scatter plot for y = x^2
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')
plt.legend()
plt.grid(True)
plt.show()