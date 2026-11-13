# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/13/2026
# Purpose: Create Arrays.
# Usage: ./lab7a.py

# TO DO 1: Create array1 and array2 according to instructions given in readme.md file.

# TO DO 2: Create array3 according to instructions given in readme.md file.

# TO DO 3: Create array4 according to instructions given in readme.md file.

import numpy as np
grid=[[num+(row*3)+1 for num in range(3)] for row in range(3)]
grid2=[[num+(row*3)+1 for num in range(4,7)] for row in range(4,7)]
array3=np.array([grid,grid2])
print(array3)
print("shape is", array3.shape)
print("dimension is", array3.ndim)
array4=np.arange(18).reshape(2,3,3)
print(array4)
