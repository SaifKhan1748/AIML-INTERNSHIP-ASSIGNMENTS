'''
Assignment (20/02/2026)
Assignment Name : NumPy Speed Test
Description : Compare Python lists vs NumPy arrays with 1M numbers,
measure execution time, write 3 observations.
'''

import time
import numpy as np

# Create 1 Million Numbers
n = 1000000


# Using Python List

start = time.time()

python_list = list(range(n))
python_result = [x * 2 for x in python_list]

end = time.time()
print("Python List Time:", end - start)


# Using NumPy Array

start = time.time()

np_array = np.arange(n)
np_result = np_array * 2

end = time.time()
print("NumPy Array Time:", end - start)