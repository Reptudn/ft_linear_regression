#!/usr/bin/python3
import sys

import matplotlib.pyplot # just to display the graph
import pandas  # just for loading the csv effecively

import shared

theta0: float = 0
theta1: float = 0

argv = sys.argv

if len(argv) != 4:
    print("Usage: python3 train.py <csv datasheet> <epochs> <learning rate>")
    sys.exit(1)

try:
    DATA_CSV = pandas.read_csv(argv[1])
    EPOCHS = int(argv[2]) # how often
    L = float(argv[3]) # the bigger the learning rate the easier it is to overshoot the minimum thetas
except ValueError:
    print(
        "ERROR: The CSV file need to be accessable from the given path and the epochs(int) and learning(float) var needs to be their reaspective type"
    )
    sys.exit(1)

# normalizing to prevent overflow
km_mean = DATA_CSV["km"].mean()
km_std = DATA_CSV["km"].std()
price_mean = DATA_CSV["price"].mean()
price_std = DATA_CSV["price"].std()

DATA_CSV["km"] = (DATA_CSV["km"] - km_mean) / km_std
DATA_CSV["price"] = (DATA_CSV["price"] - price_mean) / price_std


# returns the updated theta0 and theta1 values after one epoch
def linear_regression(theta0_curr, theta1_curr, points) -> tuple[float, float]:
    theta0_tmp: float = 0.0
    theta1_tmp: float = 0.0

    m = len(points)
    for i in range(m):
        km = points.iloc[i].km
        price = points.iloc[i].price

        error = shared.estimatePrice(km, theta0_curr, theta1_curr) - price # error: predicted - actual price

        theta0_tmp += error
        theta1_tmp += error * km

    theta0_tmp = L * (1 / m) * theta0_tmp
    theta1_tmp = L * (1 / m) * theta1_tmp

    return theta0_tmp, theta1_tmp


try:
    for i in range(EPOCHS):
        if i % 50 == 0:
            print(f"{i} - Theta0 is now: {theta0}")
            print(f"{i} - Theta1 is now: {theta1}")
        theta0_tmp, theta1_tmp = linear_regression(theta0, theta1, DATA_CSV)
        theta0 -= theta0_tmp # when theta0 is too big the error will be bigger so we subtract (go downhill)
        theta1 -= theta1_tmp # same logic as theta0 but for the slope
except KeyboardInterrupt:
    print("\n\nTraining interrupted.")
    print("Using the last known values for theta0 and theta1\n\n")


# normalize the values back
theta1_orig = theta1 * (price_std / km_std)
theta0_orig = theta0 * price_std - theta1_orig * km_mean + price_mean

print(f"Theta0 (original scale): {theta0_orig}")
print(f"Theta1 (original scale): {theta1_orig}")
print()
print("Predict the price with: python3 predict.py")

try:
    with open("theta.txt", "w") as f:
        f.write(f"{theta0_orig}\n")
        f.write(f"{theta1_orig}\n")
except FileNotFoundError:
    print("Could not write to theta.txt")

matplotlib.pyplot.scatter(DATA_CSV.km, DATA_CSV.price, color="black")
matplotlib.pyplot.plot(DATA_CSV.km, theta0 + theta1 * DATA_CSV.km)
matplotlib.pyplot.title("Linear Regression")
try:
    matplotlib.pyplot.show()
except KeyboardInterrupt:
    print("Bye Bye")
