import matplotlib.pyplot as plt
from random import randint

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]

x_values = list(range(2, max_result + 1))
plt.bar(x_values, frequencies)
plt.title("Results of Rolling Two D6 Dice 1,000 Times (Matplotlib)")
plt.xlabel("Result")
plt.ylabel("Frequency of Result")
plt.show()

from random import choice
from plotly.graph_objs import Scatter, Layout
from plotly import offline

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)

rw = RandomWalk(5000)
rw.fill_walk()

data = [Scatter(x=rw.x_values, y=rw.y_values, mode='lines', line=dict(width=1))]
layout = Layout(title="Random Walk Visualization (Plotly)",
                xaxis=dict(title='X Position'),
                yaxis=dict(title='Y Position'))
offline.plot({'data': data, 'layout': layout}, filename='random_walk_plotly.html')