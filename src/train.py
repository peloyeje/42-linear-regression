import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

class LinearRegression(object):
    def __init__(self, learning_rate, iterations):
        data = np.genfromtxt('../data/data.csv', delimiter=',', skip_header=1)
        self.price = data[:, 1]
        self.kms = data[:, 0]

        self.mean_kms = np.mean(self.kms)
        self.std_kms = np.std(self.kms)
        self.norm_kms = (self.kms - self.mean_kms)/self.std_kms

        self.mean_price = np.mean(self.price)
        self.std_price = np.std(self.price)
        self.norm_price = (self.price - self.mean_price)/self.std_price

        self.theta0 = 0
        self.theta1 = 0

        self.learning_rate = learning_rate
        self.iterations = iterations

    def estimatePrice(self, theta0, theta1, mileage):
        return theta0 + theta1 * mileage

    def vec_estimatePrice(self, theta0, theta1):
        return np.vectorize(lambda x : self.estimatePrice(theta0, theta1, x))

    def new_thetas(self, theta0, theta1, kms):
        vfunc = self.vec_estimatePrice(theta0, theta1)
        theta0_grad = 2 * np.mean(vfunc(kms) - self.norm_price)
        theta1_grad = 2  * np.mean((vfunc(kms) - self.norm_price) * kms)
        theta0 = theta0 - theta0_grad * self.learning_rate
        theta1 = theta1 - theta1_grad * self.learning_rate
        return theta0, theta1

    def train(self, verbose=True):
        all_theta0 = np.empty((0,1))
        all_theta1 = np.empty((0,1))
        for i in range(self.iterations):
            self.theta0, self.theta1 = self.new_thetas(self.theta0, self.theta1, self.norm_kms)
            all_theta0 = np.append(all_theta0, np.array([[self.theta0]]), axis = 0)
            all_theta1 = np.append(all_theta1, np.array([[self.theta1]]), axis = 0)

        self.all_theta0 = self.std_price * all_theta0 - all_theta1 * self.mean_kms * (self.std_price / self.std_kms) + self.mean_price
        self.all_theta1 = all_theta1* (self.std_price / self.std_kms)

        if verbose == True:
            np.savetxt('../output/thetas.txt', [self.all_theta0[-1], self.all_theta1[-1]], delimiter=',')
            print("The thetas have been uploaded into ../output/thetas.txt")

    def plot_loss(self):
        self.train(verbose=False)
        predictions = self.all_theta0 + self.all_theta1 * self.kms
        loss = np.average(np.square(predictions - self.price), axis=1)
        plt.plot(loss)
        plt.show()

        return loss

    #def plot_linear(self):
    #    self.train(verbose=False)
    #    theta0, theta1 = self.all_theta0[-1], self.all_theta1[-1]
