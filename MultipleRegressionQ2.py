import numpy as np

class OrdinaryLeastSquares(object):
    """
    A class defining Ordinary Least Squares as a simple implementation of a multiple linear regression model.
    The class assumes we have our features as X and the target variable as y. Expressing the model happens with
    y=bX+e, where y is the target variable vector, X is a matrix of features, b is a vector of parameters (coefficients
    that we'll want to estimate, and e is an error term.
    We obtain the coefficients with the following formula b = (transpose(X)*X)^(-1) * transpose(X)*y

    """

    def __init__(self):
        self.coefficients = []

    def _concatenate_ones(self, X):
        ones = np.ones(shape = X.shape[0]).reshape(-1, 1)
        return np.concatenate((ones, X), 1)

    def fit(self, X, y):
        if len(X.shape) == 1: X = X.reshape(-1,1)

        X = self._concatenate_ones(X)
        self.coefficients = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose()).dot(y)

    def predict(self, entry):
        b0 = self.coefficients[0]
        other_betas = self.coefficients[1:]
        prediction = b0

        for xi, bi in zip(entry, other_betas): prediction += (bi * xi)
        return prediction