
import numpy as np

def estimatePriceAsk(theta0, theta1):
    mileage = int(input("What is the mileage of your car ?"))
    return print(theta0 + theta1 * mileage)

def estimatePrice(theta0, theta1, mileage):
    return theta0 + theta1 * mileage

if __name__ == '__main__':
    theta0 = 0
    theta1 = 0
    estimatePriceAsk(theta0, theta1)
