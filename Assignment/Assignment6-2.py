from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split train-test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# KNN Model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predictions
pred = knn.predict(X_test)

# Print correct and wrong predictions
for i in range(len(y_test)):
    if pred[i] == y_test[i]:
        print(f"Correct: Predicted={pred[i]}, Actual={y_test[i]}")
    else:
        print(f"Wrong:    Predicted={pred[i]}, Actual={y_test[i]}")
