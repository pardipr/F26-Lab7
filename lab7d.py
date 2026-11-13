# Author: Pardip Rooprai
# Date: 11/13/2026
# Usage: ./lab7d.py
# Creating a 2D NumPy array

import numpy as np
arr_2d=np.array([[10, 20, 30, 40, 50],
                [60, 70, 80, 90, 100],
                [110, 120, 130, 140, 150],
                [160, 170, 180, 190, 200]
                ])
print(arr_2d)
slice_1=arr_2d[:2,-3:]
print("first two rows and last three columns\n",slice_1)
middle=arr_2d[1:3,1:3]
print("middle 2x2 subarray\n",middle)
slice3=arr_2d[::2,::2]
print("printing every other row and every other column",slice3)

