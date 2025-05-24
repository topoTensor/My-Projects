import numpy as np
import sklearn.metrics
from sklearn.preprocessing import StandardScaler
import pandas as pd
import sklearn

np.random.seed(42)

# Load data
ames_housing = pd.read_csv("ames.csv")

# Split data
train, test = sklearn.model_selection.train_test_split(ames_housing, test_size=0.8)

# Select features
X = train[['price', 'area', 'Year.Built', 'Total.Bsmt.SF', 'Garage.Area']].values
Y = train['Lot.Area'].values

# Handle NaNs
X = np.nan_to_num(X, nan=0)
Y = np.nan_to_num(Y, nan=0)

# Normalize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Normalize Y
Y = (Y - np.mean(Y)) / np.std(Y)

Lambda = 0.1  # Regularization strength

# Lasso loss function
def W_hat(w):
    return (Y - X @ w).T @ (Y - X @ w) + Lambda * np.linalg.norm(w, 1)

# Corrected gradient function
def lasso_gradient(w):
    return 2 * X.T @ (X @ w - Y) + Lambda * np.sign(w)

# Fixed gradient descent
def Gradient_Descent(func, grad_func, num_of_features, guess, gamma=0.01, epsilon=1e-5, max_iters=10000):
    w = guess
    for _ in range(max_iters):
        grad = grad_func(w)
        if np.linalg.norm(grad) < epsilon:
            break
        w -= gamma * grad
    return w

# Run Lasso regression
def lasso():
    r = np.random.rand(X.shape[1])
    W = Gradient_Descent(W_hat, lasso_gradient, X.shape[1], r)

    Y_hat = X @ W  # Predictions

    mse = sklearn.metrics.mean_squared_error(Y, Y_hat)
    mae = sklearn.metrics.mean_absolute_error(Y, Y_hat)
    r2 = sklearn.metrics.r2_score(Y, Y_hat)

    print(f"Lasso, lambda={Lambda}: {W}")
    print(f"MSE: {mse}, MAE: {mae}, R²: {r2}")
    return r2

lasso()
