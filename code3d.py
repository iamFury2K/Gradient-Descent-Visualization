import numpy as np
import matplotlib.pyplot as plt

def function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5

def calc_gradient(x, y):
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)

x = np.arange(-1, 1, 0.01)
y = np.arange(-1, 1, 0.01)

X, Y = np.meshgrid(x, y)

Z = function(X, Y)
learning_rate = 0.01
current_pos = (0.7, 0.5, function(0.7, 0.5))

ax = plt.subplot(projection='3d', computed_zorder=False)
for _ in range(1000):
    x_derivative, y_derivative = calc_gradient(current_pos[0], current_pos[1])
    x_new, y_new = current_pos[0] - learning_rate * x_derivative, current_pos[1] - learning_rate * y_derivative
    current_pos = (x_new, y_new, function(x_new, y_new))
    
    ax.plot_surface(X,Y,Z, cmap='viridis')
    ax.scatter(current_pos[0], current_pos[1], current_pos[2], color='magenta', zorder=1)
    plt.pause(0.01)
    ax.clear()