import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

PI=3.14
T=PI/4 

r = lambda t: t
phi = lambda t: t

r_hat = lambda t: np.array([np.cos(phi(t)), np.sin(phi(t))])
phi_hat = lambda t: np.array([-np.sin(phi(t)), np.cos(phi(t))])

J=lambda t : r(t)*np.array([[np.cos(phi(t)), np.sin(phi(t))], [np.sin(phi(t)), -np.cos(phi(t))]])

fig, ax = plt.subplots()

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_aspect('equal')

point = r(T) * r_hat(T) 

# Initial vectors

r_vector = ax.quiver(point[0], point[1], r_hat(T)[0], r_hat(T)[1], scale=1, color='r', alpha=0.7, angles='xy', scale_units='xy')
phi_vector = ax.quiver(point[0], point[1], phi_hat(T)[0], phi_hat(T)[1], scale=1, color='b', alpha=0.7, angles='xy', scale_units='xy')
point_quiver = ax.quiver(0,0, point[0], point[1], scale=1, color='black', alpha=0.7, angles='xy', scale_units='xy')
path = ax.scatter([], [])
historyX=[]
historyY=[]

def update(frame):
    t = frame /10

    q=r(t)*r_hat(t)
    historyX.append(q[0])
    historyY.append(q[1])

    coords = np.column_stack((historyX, historyY))
    path.set_offsets(coords)
    
    point_quiver.set_UVC(q[0],q[1])
    
    r_vector.set_offsets(q)
    phi_vector.set_offsets(q)

    r_vector.set_UVC(r_hat(t)[0], r_hat(t)[1])
    phi_vector.set_UVC(phi_hat(t)[0], phi_hat(t)[1])
    # print(np.linalg.norm(r(t)),np.linalg.norm(r_hat(t)),np.linalg.norm(phi(t)),np.linalg.norm(phi_hat(t)))
    
    return r_vector, phi_vector, point_quiver,path

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0.1, 100, 200), interval=50)
plt.show()
