import numpy as np

class LinearRegression:
    def __init__(self, lr=0.01, max_iterations=1000, threshold=1e-4):
        self.lr = float(lr)
        self.max_iterations = int(max_iterations)
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

    def _intercept(self, X):
        return np.c_[np.ones(X.shape[0]), X]

    def _descale_beta(self, b):
        """Denormalize weights"""
        b = b.copy()
        b[0] = b[0] - (self.mean/self.std)
        b[1] = b[1] / self.std
        return b

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

        history: np.array
            Performance history of the convergence process
            Each row contains : the beta parameters and the loss

        """

        # Scale dataset
        X = self._scale(X)
        # Add intercept column
        X = self._intercept(X)
        # Initialize weight vector
        self.beta = np.zeros(X.shape[1])
        self.history = np.zeros((self.max_iterations, 4))

        # Iterate until we reach convergence or maximum number of iterations
        for i in range(self.max_iterations):
            # Compute gradient
            error = self._model(X, self.beta) - y
            gradient = (2.0/X.shape[0]) * np.dot(X.T, error)

            # Update beta according to learning rate
            beta = self.beta - (self.lr * gradient)
            loss = self._loss(
                self._model(X, beta),
                y
            )

            # Store history
            self.history[i, :] = (i, *beta, loss)

            if np.sum(np.abs(beta - self.beta)) < self.threshold:
                # We reached sufficient precision, let's exit the loop
                print(f'Convergence reached in {i} iterations, exiting the loop ...')
                break
            else:
                # We store the new weights
                self.beta = beta

            # Print info on the current iteration if needed
            if verbose and i % 10 == 0:
                print(
                    f'[{i:5}] Loss: {loss:20} | Beta: {self._descale_beta(self.beta)}')

        # When convergence is reached, denormalize the beta vector and store it
        self.beta = self._descale_beta(self.beta)

        return self.beta, self.history

    def predict(self, X):
        X = self._intercept(X)
        return self._model(X, self.beta)
