import numpy as np
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=100, n_features=1,
                       n_informative=1, noise=10, random_state=10)

def linear_normal_equation(X, y):
    X_transpose = np.transpose(X)
    X_transpose_X = np.dot(X_transpose, X)
    X_transpose_y = np.dot(X_transpose, y)

    try:
        theta = np.linalg.solve(X_transpose_X, X_transpose_y)
        return theta
    except np.linalg.LinAlgError:
        print("Error")

X_with_intercept = np.c_[np.ones((X.shape[0], 1)), X] # Добавление столбца для свободного члена (theta(0))
print(X_with_intercept)

theta = linear_normal_equation(X_with_intercept, y)
if theta is not None:
    print(theta)
else:
    print("Unable to compute theta. The matrix X_transpose_X is singular.")


def predict(X, theta):
    predictions = np.dot(X, theta)
    return predictions
