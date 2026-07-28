import numpy as np
print(np.__version__)

import matplotlib.pyplot as plt

# 1. Define your data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 2. Create the plot type
plt.plot(x, y, color="blue", linestyle="--", marker="o")

# 3. Add titles and axis labels
plt.title("Sample Line Chart")
plt.xlabel("X Axis Label")
plt.ylabel("Y Axis Label")

# 4. Display the plot window
plt.show()