

import matplotlib.pyplot as plt 

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, marker='o', linewidth=2)
plt.title("First Five Cubic Numbers", fontsize=16)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Cube of Value", fontsize=12)
plt.show()

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, s=5)
plt.title("Cubic Numbers (1-5000)", fontsize=16)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Cube of Value", fontsize=12)
plt.show()