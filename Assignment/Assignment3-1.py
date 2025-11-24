import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
x = np.array([2, 3, 4, 5, 6, 7, 8])
y = np.array([4, 5, 6, 7, 8, 9, 10])

# Correlation matrix
corr_matrix = np.corrcoef(x, y)

# Correlation coefficient
corr_coef = np.corrcoef(x, y)[0, 1]

# Scatter plot
plt.scatter(x, y, color='blue')
plt.title("Scatter Plot between X and Y")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()

print("Correlation Matrix:\n", corr_matrix)
print("Correlation Coefficient (r):", corr_coef)
