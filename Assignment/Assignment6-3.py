# Heart Attack Prediction – Model Comparison

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("heart.csv")   # dataset from Kaggle

# Features and Target
X = df.drop("target", axis=1)
y = df["target"]

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -----------------------------
# Standardization
# (needed for Logistic & KNN)
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

results = {}

# -----------------------------
# Logistic Regression
# -----------------------------
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train_scaled, y_train)
pred_lr = log_reg.predict(X_test_scaled)
results["Logistic Regression"] = accuracy_score(y_test, pred_lr)

# -----------------------------
# Decision Tree
# -----------------------------
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
pred_dt = dt.predict(X_test)
results["Decision Tree"] = accuracy_score(y_test, pred_dt)

# -----------------------------
# Random Forest
# -----------------------------
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)
results["Random Forest"] = accuracy_score(y_test, pred_rf)

# -----------------------------
# K-Nearest Neighbors
# -----------------------------
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
pred_knn = knn.predict(X_test_scaled)
results["KNN"] = accuracy_score(y_test, pred_knn)

# -----------------------------
# Print Results
# -----------------------------
print("\nModel Accuracy on Test Data:")
for model, acc in results.items():
    print(f"{model} : {acc:.4f}")

# -----------------------------
# Best Model
# -----------------------------
best_model = max(results, key=results.get)
print(f"\nBest Performing Model: {best_model}")
