import numpy as np
from functions import modifier, grade_stats, matrix_manipulator


modifier_data = np.array([[1,2,3],[2,3,4],[5,6,7]])
modifier(modifier_data)

grade_data = np.array([
    [123456, 9, 8, 0, 2],
    [234567, 8, 8, 0, 5],
    [345678, 9, 8, 6, 10],
    [456789, 8, 7, 7, 10]
])
grade_stats(grade_data)


A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[5, 6], 
              [7, 8]])
matrix_manipulator(A,B)