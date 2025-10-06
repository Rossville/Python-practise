# Assignment 1 - Data Science Lab

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm

def program1():
    #numpy ->
    arr = np.random.randint(1,20, size=10)
    print(f"Original Array: {arr}")

    print(f"Mean of the given array: {np.mean(arr)}")
    print(f"Sum of the given array: {np.sum(arr)}")
    print(f"Sorted arr: {np.sort(arr)}")

    #pandas ->
    data: object = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [24, 30, 22, 35, 29],
        'Score': [85, 90, 78, 88, 92]
    }
    df = pd.DataFrame(data)
    print(f"Data Frame :")
    print(df)

    print(f"Average age: {df['Age'].mean()}")
    print(f"Maximum Score : {df['Score'].max()}")
    print("Summary Statistics :\n", df.describe())

    # Matplotlib
    plt.figure(figsize=(5,5))
    plt.bar(df['Name'], df['Score'], color='red', edgecolor="black")
    plt.xlabel("Students")
    plt.ylabel("Scores")
    plt.title("Scores of Students")
    plt.show()



def program2():
    # ---------------- Sample Data ----------------
    data = [12, 15, 14, 10, 18, 20, 15, 12, 17, 14, 15, 16, 14, 18, 20, 19, 15, 12, 14, 16]
    series = pd.Series(data)

    # ---------------- Frequency Distribution ----------------
    freq_dist = series.value_counts().sort_index()
    print("Frequency Distribution:\n", freq_dist)

    # Plot frequency distribution
    plt.figure(figsize=(7,5))
    freq_dist.plot(kind="bar", color="lightgreen", edgecolor="black")
    plt.title("Frequency Distribution")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

    # ---------------- Averages ----------------
    mean_val = np.mean(data)
    median_val = np.median(data)
    mode_val = series.mode().values[0]   # Pandas handles multiple modes

    print("\nAverages:")
    print("Mean:", mean_val)
    print("Median:", median_val)
    print("Mode:", mode_val)

    # ---------------- Variability ----------------
    variance_val = np.var(data, ddof=1)   # Sample variance (ddof=1)
    std_dev_val = np.std(data, ddof=1)    # Sample standard deviation
    range_val = np.max(data) - np.min(data)

    print("\nVariability:")
    print("Variance:", variance_val)
    print("Standard Deviation:", std_dev_val)
    print("Range:", range_val)

    # ---------------- Histogram ----------------
    plt.figure(figsize=(7,5))
    plt.hist(data, bins=6, color="skyblue", edgecolor="black")
    plt.title("Histogram of Data")
    plt.xlabel("Bins")
    plt.ylabel("Frequency")
    plt.show()


def program3():
    # ---------------- Normal Distribution ----------------
    # Define mean and standard deviation
    mean = 0
    std_dev = 1

    # Generate x values
    x = np.linspace(-4, 4, 1000)

    # Compute probability density function (PDF)
    y = norm.pdf(x, mean, std_dev)

    # ---------------- Plot Normal Curve ----------------
    plt.figure(figsize=(8,5))
    plt.plot(x, y, color="blue", label=f"N({mean}, {std_dev}²)")
    plt.fill_between(x, y, color="skyblue", alpha=0.4)

    plt.title("Normal Distribution Curve")
    plt.xlabel("X values")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.grid(True)
    plt.show()

    # ---------------- Multiple Normal Curves ----------------
    # Show curves with different means and variances
    means = [0, 0, 0]
    std_devs = [0.5, 1, 2]

    plt.figure(figsize=(8,5))
    for sd in std_devs:
        y = norm.pdf(x, 0, sd)
        plt.plot(x, y, label=f"Mean=0, StdDev={sd}")

    plt.title("Comparison of Normal Curves")
    plt.xlabel("X values")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    # program1()
    # program2()
    program3()

if __name__ == "__main__":
    main()
