import numpy as np
from linear_regression import LinearRegression

data = np.loadtxt('../data/data.csv', delimiter=',', skiprows=1)
X = data[:, 0]
y = data[:, 1]

lr = LinearRegression()
lr.fit(X, y)
print(lr.predict(X))
