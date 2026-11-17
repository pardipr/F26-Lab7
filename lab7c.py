# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 11/13/2026
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

# TO DO 1: Create numArray according to instructions given in readme.md file.

# TO DO 2: Perform the operations on numArray given in readme.md file.

# TO DO 3: Run the script.
import numpy as np
arr=np.random.rand(100)
slice_1 = arr[:10]
print("\nfirst 10 values of Sliced 1D Array):\n", slice_1)
slice_2=arr[-10:]
print("\nlast 10 values of Sliced 1D Array):\n", slice_2)
slice_3=arr[21:51]
print("\n 30 values starting from index 21 of 1D array\n:", slice_3)
np.put(arr,[num for num in range(50,66)], 101)
print("\nnew values at index 50 to 65 of 1D array\n",arr[50:66])

