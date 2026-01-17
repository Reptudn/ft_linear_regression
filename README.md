# ft_linear_regression
Car price prediction

## How to run
1. simply run `source .venv/bin/activate` to enter the venv
2. Train the model by running `python3 train.py <csv datasheet> <epochs> <learning rate>`
> Once the training is done you will get the theta0 and theta1 printed to the console
3. Run the prediction with `python3 predict.py <theta0> <theta1>` and you will be able to enter the cars mileage and then get the estimated price.

## Whats those weird words?
### epochs
This is basically the amount of times the model tries to reduce the error rate. Or in simple words: Its the amount of iterations of the loop.

### Learning rate
This is the amount of steps done each epoch to try to reduce the error rate.
> The smaller the steps the longer it will take to train but the better the data will be.

### Theta0 and Theta1
Imagine math class back then.. y = m*x+b
-> m is Theta0
-> b is Theta1