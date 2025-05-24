import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

import gradient

np.random.seed(42)

ames_housing = pd.read_csv("ames.csv")

train,test=sklearn.model_selection.train_test_split(ames_housing, test_size=0.8)

num_of_features=6
X=train[['price', 'area','Year.Built', 'Total.Bsmt.SF', 'Garage.Area']]
Y=train['Lot.Area']

X = (X - np.min(X, axis=0)) / (np.max(X, axis=0) - np.min(X, axis=0))
X = np.hstack((np.ones((X.shape[0], 1)), X))

X_T_X=X.T@X

def regression():
    W=np.linalg.inv(X_T_X)@(X.T@Y)

    Y_hat=X@W
    mse=sklearn.metrics.mean_squared_error(Y,Y_hat)
    mae=sklearn.metrics.mean_absolute_error(Y,Y_hat)
    r2=sklearn.metrics.r2_score(Y,Y_hat)
    # print("without lambda: ",W,":",mse,mae,r2)
    return r2

def ridge():
    Lambda=5000
    W_ridge=np.linalg.inv(X_T_X+Lambda*np.eye(X_T_X.shape[0]))@(X.T@Y)
    Y_hat_ridge=X@W_ridge

    mse=sklearn.metrics.mean_squared_error(Y,Y_hat_ridge)
    mae=sklearn.metrics.mean_absolute_error(Y,Y_hat_ridge)
    r2=sklearn.metrics.r2_score(Y,Y_hat_ridge)
    # print(f"ridge, lambda={Lambda}: ",W_ridge,":",mse,mae,r2)
    return r2

def lasso():
    Lambda=0.1
    def W_hat(w):
        residuals = Y - X @ w
        return np.sum(residuals**2) / len(Y)  # Normalize by N

    r = np.random.randn(num_of_features) * 0.01


    W=gradient.Gradient_Descent(W_hat, num_of_features, r)

    Y_hat=X@W

    mse=sklearn.metrics.mean_squared_error(Y,Y_hat)
    mae=sklearn.metrics.mean_absolute_error(Y,Y_hat)
    r2=sklearn.metrics.r2_score(Y,Y_hat)
    print(f"lasso, lambda={Lambda}: ",W,":",mse,mae,r2)
    return r2

r2_reg=regression()
r2_ridge=ridge()
r2_lasso=lasso()

print(r2_reg, r2_ridge, r2_lasso)