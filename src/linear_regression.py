import numpy as np

class LinearRegression:
    def __init__(self, lr=0.01, max_iter=1000, threshold=1e-4):
        self.lr = float(lr)
        self.max_iter = int(max_iter)
        self.threshold = float(threshold)

    @staticmethod
    def _model(X, b):
        """Basic linear regression model"""
        return np.dot(X, b)

    @staticmethod
    def _loss(y_true, y_pred):
        """Computes the MSE"""
        if len(y_true) != len(y_pred):
            raise ValueError(
                'Length mismatch between ground truth and prediction vector')
        return np.mean((y_true - y_pred) ** 2)

    def _scale(self, X):
        """Normalize data"""
        self.mean = X.mean(axis=0)
        self.std = X.std(axis=0)
        return (X - self.mean) / self.std

    def fit(self, X, y, verbose=True):
        """Learns the weights of the regression model

        Parameters
        ----------
        X: np.array
            Training data
        y: np.array
            Target

        Returns
        -------
        beta: np.array
            Vector of model weights

        i: int
            Number of iterations until convergence

        loss: float
            MSE

        """

        # Scale dataset
        X = self._scale(X)
        # Add intercept column
        X = np.c_[np.ones(X.shape[0]), X]
        # Initialize weights and iterations counter
        self.beta = np.zeros(X.shape[1])

        # Iterate until we reach convergence or maximum number of iterations
        for i in range(self.max_iter):
            # Compute gradient
            error = self._model(X, self.beta) - y
            gradient = (2.0/X.shape[0]) * np.dot(X.T, error)

            # Update beta according to learning rate
            beta = self.beta - (self.lr * gradient)

            if np.sum(np.abs(beta - self.beta)) < self.threshold:
                # We reached sufficient precision, let's exit the loop
                print(f'Convergence reached in {i} iterations, exiting the loop ...')
                break
            else:
                # We store the new weights
                self.beta = beta

            # Print info on the current iteration if needed
            if verbose and i % 10 == 0:
                loss = self._loss(self._model(X, self.beta), y)
                print(
                    f'[{i:5}] Loss: {loss:20} | Beta: {self.beta}')


        return self.beta, i, self._loss(self._model(X, self.beta), y)
