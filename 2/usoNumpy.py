import numpy as np
from numpy.linalg import matrix_power
# matrix equiv. of the imaginary unit
i = np.array([[-3, 3, 2], [-8, 7, 4], [8, -6, -3]])
matrix = matrix_power(i, 3)  # should = -i
print matrix
