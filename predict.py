#!/usr/bin/python3
import sys

import shared

try:
    with open("theta.txt", "r") as f:
        theta0 = f.readline().strip()
        theta1 = f.readline().strip()
except FileNotFoundError:
    print("Could not read theta.txt!\nUsing default values.")
    theta0 = 0
    theta1 = 0

try:
    theta0 = float(theta0)
    theta1 = float(theta1)
except ValueError:
    print("theta0 and theta1 both have to be valid float values!")
    sys.exit(1)

print("ft_linear_progression (by jkauker)\n")
print(f"Theta0: {theta0}")
print(f"Theta1: {theta1}")
print()
try:
    while True:
        mileage = input("Enter the car milege: ")
        try:
            mileage = float(mileage)
        except ValueError:
            print(f"Failed to convert mileage to a useable float value: {mileage}")
            print("Try again...\n")
            continue

        print(
            f"The estimated price is: {shared.estimatePrice(mileage, theta0, theta1):.2f}eur\n"
        )
except KeyboardInterrupt:
    print("\n\nThanks for using the price estimator.")
