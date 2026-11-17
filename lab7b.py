# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/13/2026
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py

# TO DO 1: Copy the code from your lab7a.py file and paste here.
import numpy as np
array1=np.arange(20,50)
array2=np.array(list(range(20,50)))
print("Array1 is")
print(array1)
print("Array2 is")
print(array2)

grid=[[num+(row*3)+1 for num in range(3)] for row in range(3)]
grid2=[[num+(row*3)+1 for num in range(4,7)] for row in range(4,7)]
array3=np.array([grid,grid2])
print("Array3 is")
print(array3)
print("shape is", array3.shape)
print("dimension is", array3.ndim)

array4=np.array(["Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]).reshape(2,3,2)
print("Array4 is")
print(array4)
print("shape is", array4.shape)
print("dimension is", array4.ndim)

# TO DO 2: Reshape array1 reshapes array2 according to instructions given in readme.md file.
array1=array1.reshape(5,6)
array2=array2.reshape(2,3,5)
print("The reshape of 5x6 shape (5 rows, 6 columns) for array1 is")
print(array1)
print("The reshape of 2x3x5 (a 3D matrix) for array2 is")
print(array2)

# TO DO 3: Create array5 according to instructions given in readme.md file.
array5=np.diag([45,7,61,8,9])
print("Array5 is")
print(array5)

# TO DO 4: Create array6 according to instructions given in readme.md file.
array6=np.random.rand(7,7)
print("Array6 is")
print(array6)

# TO DO 5: Run the script.

