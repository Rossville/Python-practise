import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

# Model training
model = LinearRegression()
model.fit(x, y)

# Predictions
y_pred = model.predict(x)

# Coefficients
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])

# Plot
plt.scatter(x, y, color='blue', label='Actual')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.title("Simple Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
