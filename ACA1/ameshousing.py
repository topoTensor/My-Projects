import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

ames_housing = pd.read_csv("AmesHousing.csv")

feat1='Lot Area'
feat2='Year Built'
X=ames_housing[[feat1,feat2]]
Y=ames_housing['SalePrice']

model=sklearn.linear_model.LinearRegression()
model.fit(X,Y)

n_points=100
feat1_vals=np.linspace(X[feat1].min(),X[feat1].max(),n_points)
feat2_vals=np.linspace(X[feat2].min(),X[feat2].max(),n_points)

xv,yv=np.meshgrid(feat1_vals,feat2_vals)

Z=model.predict(np.array([xv.ravel(),yv.ravel()]).T)
Z=Z.reshape(xv.shape)


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[feat1], X[feat2], Y, color='red', alpha=0.2)

ax.plot_surface(xv, yv, Z, color='blue', alpha=0.2)

ax.view_init(25, 15)

ax.set_xlabel(feat1)
ax.set_ylabel(feat2)
ax.set_zlabel('House Price')

plt.title('3D Plot of House Price with Fitted Plane')
plt.grid(True)
plt.show()



# for (i,x) in enumerate(X):
#     if x > 50000:
#         del X[i]
#         del Y[i]

# mean_x = X.mean()
# mean_y = Y.mean()

# w1= np.sum((X-mean_x)*(Y-mean_y)) / np.sum((X-mean_x)**2)
# w0=mean_y-w1*mean_x

# y_hat=w0+w1*X

# mse=sklearn.metrics.mean_squared_error(Y, y_hat)
# r2=sklearn.metrics.r2_score(Y,y_hat)
# print(mse,r2)

# plt.plot(X,y_hat,color='red')

# plt.rcParams["figure.figsize"] = (15,4)
# plt.scatter(X,Y,alpha=0.5)
# plt.show()