import numpy as np
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data
import nnfs

# x_train is the input variable (size in 1000 square feet)
# y_train is the target (price in 1000s of dollars)
nnfs.init()

X, y = spiral_data(samples=100, classes=3)
plt.scatter(X[:,0], X[:,1])
plt.show()