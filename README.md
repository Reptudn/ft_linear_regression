# ft_linear_regression
Car price prediction

## How to run
1. simply run `source .venv/bin/activate` to enter the venv
2. Train the model by running `python3 train.py <csv datasheet> <epochs> <learning rate>` (the more epochs the better)
> Once the training is done you will get the theta0 and theta1 printed to the console
3. Run the prediction with `python3 predict.py` and you will be able to enter the cars mileage and then get the estimated price.

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

# How does this work? Is this magic?
> We want to find a line with the least error rate.
> Line function: y = mx + b -> The estimatePrice() func
>
> y is the price we want to predict
> x is the mileage we enter
> theta1 is the slope aka m
> theta0 is the bias aka b

## Calculate the MSE (mean squared error):
> Basically for each point Predicted_Price - Actual_Price

For each point we need to calculate this and the lower the MSE is the better our line function is aka our thetas.

## Algo
- Define a start point -> default values for theta0 and theta1
- We go downhill after every step a bit (defined by the learning rate)
  - The bigger the learning rate the less the chance to find the best theta values because we might overshoot it and "bounce around" the perfect minimum
- after each epoch, both thetas are returned and depending on if they are positive or negative they are adjusted by subtracting the error and multiplied by the learning rate to find the slope ( theta1 * the mileage of the current point)