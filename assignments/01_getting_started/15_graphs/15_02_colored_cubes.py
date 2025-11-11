import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.figure(figsize=(10, 3))
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, s=10)
plt.title("Colored Cubes (1-5000)", fontsize=16)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Cube of Value", fontsize=12)
plt.show()