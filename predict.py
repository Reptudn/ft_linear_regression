import sys
import shared

argv = sys.argv

if (len(argv) != 3):
    print(f"Usage: python3 {argv[0]} theta0 theta1")
    sys.exit(1)

try:
    theta0 = float(argv[1])
    theta1 = float(argv[2])
except:
    print(f"theta0 and theta1 both have to be valid float values!")
    sys.exit(1)

print('ft_linear_progression (by jkauker)\n')
try:
    while True:
        mileage = input('Enter the car milege: ')
        try:
            mileage = float(mileage)
        except:
            print(f"Failed to convert mileage to a useable float value: {mileage}")
            print("Try again...\n")
            continue

        print(f"The estimated price is: {shared.estimatePrice(mileage, theta0, theta1)}eur\n")
except:
    print("\n\nThanks for using the price estimator.")
    sys.exit(0)

