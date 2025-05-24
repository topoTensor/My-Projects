import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def Gradient(func, domain_dimension, inputs, h=1e-6):
    # func takes np.array as imput
    derivs=np.zeros(domain_dimension)
    Hs=[]
    for i in range(domain_dimension):
        Hs.append(np.zeros(domain_dimension))
        Hs[-1][i]=h

    for i in range(domain_dimension):
        derivs[i]=(func((inputs+Hs[i]))-func(inputs))/h
    return derivs

def Gradient_Descent(func, domain_dimension, guess, gamma=0.01, epsilon=10**(-5), max_iters=1000):
    
    g = Gradient(func, domain_dimension, guess)
    x = guess - gamma * g
    iteration = 0

    while (np.abs(g) > np.array([epsilon] * domain_dimension)).any() and iteration < max_iters:
        gamma = 0.1 / (1 + 0.01 * iteration)
        x = x - gamma * g
        g = Gradient(func, domain_dimension, x)
        iteration += 1

    return x



# ___________________________
# func = lambda p: p[0]**2+p[1]**2

# xs=np.linspace(-1000,1000,25)
# ys=np.linspace(-1000,1000,25)

# Xs,Ys=np.meshgrid(xs,ys)
# Zs=func(np.array([Xs,Ys]))

# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# surf = ax.plot_surface(Xs, Ys, Zs, cmap=plt.cm.coolwarm,
#                        linewidth=0, antialiased=False, alpha=0.5)

# point = ax.scatter([], [], [], color='red', s=100)

# grad = Gradient_Descent(func, 2, np.array([-1000,1000]))

# # Function to update the point's position
# def update(frame):
#     new_x = grad[frame][0]
#     new_y = grad[frame][1]
#     new_z = func(grad[frame])

#     point._offsets3d = ([new_x], [new_y], [new_z])
#     return point


# # Create animation
# ani = animation.FuncAnimation(fig, update, frames=len(grad), interval=1, blit=False)

# plt.show()