import sys
import pandas # just for loading the csv effecively
import matplotlib # to show the data (probably not useable in the project submission due to subject restrictions)

# the training program here

argv = sys.argv

if len(argv) != 4:
    print("Usage: python3 train.py <csv datasheet> <epochs> <learning rate>")
    sys.exit(1)

DATA_CSV = argv[1]
EPOCHS = int(argv[2])
L = int(argv[2])

theta0 = 0
theta1 = 0

for i in range(EPOCHS):
    continue

print("Theta0: " + theta0)
print("Theta1: " + theta1)
print()
print(f"Predict the price with: python3 predict.py {theta0} {theta1}")