import sys
import pandas # just for loading the csv effecively
import matplotlib.pyplot # to show the data (probably not useable in the project submission due to subject restrictions)
import shared

# the training program here

argv = sys.argv

if len(argv) != 4:
    print("Usage: python3 train.py <csv datasheet> <epochs> <learning rate>")
    sys.exit(1)

try:
    DATA_CSV = pandas.read_csv(argv[1])
    EPOCHS = int(argv[2])
    L = float(argv[3])
except:
    print(f"ERROR: The CSV file need to be accessable from the given path and the epochs(int) and learning(float) var needs to be their reaspective type")
    sys.exit(1)

# normalizing to prevent overflow
km_mean = DATA_CSV['km'].mean()
km_std = DATA_CSV['km'].std()
price_mean = DATA_CSV['price'].mean()
price_std = DATA_CSV['price'].std()

DATA_CSV['km'] = (DATA_CSV['km'] - km_mean) / km_std
DATA_CSV['price'] = (DATA_CSV['price'] - price_mean) / price_std


theta0 = 0
theta1 = 0

# def gradient_descend(theta0_curr, theta1_curr, points):
#     theta0_gradient = 0
#     theta1_gradient = 0

#     n = len(points)
#     for i in range(n):
#         mileage = points.iloc[i].km
#         price = points.iloc[i].price

#         theta0_gradient += -(2/n) * mileage * (price - (theta0_curr * mileage + theta1_curr))
#         theta1_gradient += -(2/n) * (price - ((theta0_curr * price + theta1_curr)))

#     theta0 = theta0_curr - theta0_gradient * L
#     theta1 = theta1_curr - theta1_gradient * L
#     return theta0, theta1

def linear_regression(theta0_curr, theta1_curr, points):
    theta0_tmp = 0
    theta1_tmp = 0

    m = len(points)
    for i in range(m):
        km = points.iloc[i].km
        price = points.iloc[i].price

        error = shared.estimatePrice(km, theta0_curr, theta1_curr) - price

        theta0_tmp += error
        theta1_tmp += error * km

    theta0_tmp = theta0_curr - L * (1 / m) * theta0_tmp
    theta1_tmp = theta1_curr - L * (1 / m) * theta1_tmp

    return theta0_tmp, theta1_tmp

for i in range(EPOCHS):
    if (i % 50 == 0):
        print(f"{i} - Theta0 is now: {theta0}")
        print(f"{i} - Theta1 is now: {theta1}")
    theta0, theta1 = linear_regression(theta0, theta1, DATA_CSV)

# normalize the values back
theta1_orig = theta1 * (price_std / km_std)
theta0_orig = theta0 * price_std - theta1_orig * km_mean + price_mean

print(f"Theta0 (original scale): {theta0_orig}")
print(f"Theta1 (original scale): {theta1_orig}")
print()
print(f"Predict the price with: python3 predict.py {theta0_orig} {theta1_orig}")

matplotlib.pyplot.scatter(DATA_CSV.km, DATA_CSV.price, color="black")
matplotlib.pyplot.plot(DATA_CSV.km, theta0 + theta1 * DATA_CSV.km)
matplotlib.pyplot.show()