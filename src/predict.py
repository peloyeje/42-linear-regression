import numpy as np

def predict(self):
    theta0, theta1 = np.genfromtxt('../output/thetas.txt', delimiter=',')
    mileage = int(input("What is the mileage of your car ?"))
    prediction = theta0 + theta1 * mileage
    return print("The predicted price of your car is {0} euros.".format(prediction))
