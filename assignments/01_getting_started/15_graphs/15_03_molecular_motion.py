import matplotlib.pyplot as plt
from random_walk import RandomWalk # type: ignore

rw = RandomWalk(5000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(rw.x_values, rw.y_values, linewidth=1)

ax.scatter(0, 0, c='green', edgecolors='none', s=50)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()