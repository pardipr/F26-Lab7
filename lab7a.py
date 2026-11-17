# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/13/2026
# Purpose: Create Arrays.
# Usage: ./lab7a.py

# TO DO 1: Create array1 and array2 according to instructions given in readme.md file.
import numpy as np
array1=np.arange(20,50)
array2=np.array(list(range(20,50)))
print("Array1 is")
print(array1)
print("Array2 is")
print(array2)

# TO DO 2: Create array3 according to instructions given in readme.md file.
grid=[[num+(row*3)+1 for num in range(3)] for row in range(3)]
grid2=[[num+(row*3)+1 for num in range(4,7)] for row in range(4,7)]
array3=np.array([grid,grid2])
print("Array3 is")
print(array3)
print("shape is", array3.shape)
print("dimension is", array3.ndim)

# TO DO 3: Create array4 according to instructions given in readme.md file.
array4=np.array(["Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]).reshape(2,3,2)
print("Array4 is")
print(array4)
print("shape is", array4.shape)
print("dimension is", array4.ndim)
