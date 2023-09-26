import matplotlib.pyplot as plt
import statistics
import random

# Generate random data (over 100 numbers)
data = [random.randint(1, 100) for _ in range(150)]

# Line chart
plt.subplot(3, 3, 1)
plt.plot(data)
plt.title('Line Chart')

# Scatter plot
plt.subplot(3, 3, 2)
plt.scatter(range(len(data)), data)
plt.title('Scatter Plot')

# Bar plot
plt.subplot(3, 3, 3)
plt.bar(range(len(data)), data)
plt.title('Bar Plot')

# Histogram
plt.subplot(3, 3, 4)
plt.hist(data, bins=10)
plt.title('Histogram')

# Box plot
plt.subplot(3, 3, 5)
plt.boxplot(data)
plt.title('Box Plot')

# Pie plot
plt.subplot(3, 3, 6)
plt.pie(data[:5], labels=['A', 'B', 'C', 'D', 'E'])
plt.title('Pie Plot')

# Area plot
plt.subplot(3, 3, 7)
plt.fill_between(range(len(data)), data)
plt.title('Area Plot')

# Violin plot
plt.subplot(3, 3, 8)
plt.violinplot(data)
plt.title('Violin Plot')

# Heatmap
plt.subplot(3, 3, 9)
plt.imshow([data], cmap='hot', aspect='auto')
plt.colorbar()
plt.title('Heatmap')

# Adjusting layout
plt.tight_layout()

# Displaying the graphs
plt.show()

# Data statistics
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_dev = statistics.stdev(data)
variance = statistics.variance(data)

# Displaying the statistics
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
