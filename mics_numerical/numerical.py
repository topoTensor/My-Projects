import numpy as np
import matplotlib.pyplot as plt

a=np.array([[0,6,7,8],[0,3,2,4],[0,12,8,10],[0,7,5,3]], dtype=float)
b=np.array([[6,9,11,10]],dtype=float)

# b must not be transposed
def augment(M,b):
    return np.concatenate((M,b.transpose()),axis=1)

def Gaussian3(M,b):
    G=augment(M,b)
    G[1]-=(G[1][0]/G[0][0])*G[0]
    G[2]-=(G[2][0]/G[0][0])*G[0]
    
    G[2]-=(G[2][1]/G[1][1])*G[1]
    
def Gaussian4(M,b):
    G=augment(M,b)
    G[1]-=(G[1][0]/G[0][0])*G[0]
    G[2]-=(G[2][0]/G[0][0])*G[0]
    G[3]-=(G[3][0]/G[0][0])*G[0]
    
    G[2]-=(G[2][1]/G[1][1])*G[1]
    G[3]-=(G[3][1]/G[1][1])*G[1]
    
    G[3]-=(G[3][2]/G[2][2])*G[2]
    print(G)
    
# M is n*n
def sort_for_zeros(M):
    n=np.shape(M)[0]
    C=np.full((n,n),0, dtype=float)
    np.copyto(C,M)
    for i in range(0,n):
        no_null=False
        if C[i][i] == 0:
            for j in range(0,n):
                if C[j][i] != 0:
                    no_null=True
                    T=np.full((1,n),0,dtype=float)
                    np.copyto(T,C[i])
                    C[i]=C[j]
                    C[j]=T
                    break
        if no_null==False:
            break
    return C

# M is n*n
def Gaussian(M,b):
    n=np.shape(M)[1]
    G=augment(sort_for_zeros(M),b)
    for j in range(1,n):
        for i in range(j,n):
            if G[j-1][j-1]==0:
                j+=1
                continue
            G[i]-=(G[i][j-1]/G[j-1][j-1])*G[j-1]
    return G

def square_root(guess, S, accuracy):
    for i in range(accuracy):
        guess=0.5*(guess+S/guess)
    return guess

def gradient_descent(grad_f,guess,gamma, epsilon):
    point=guess
    g=np.array(grad_f[0](point[0],point[1]),grad_f[1](point[0],point[1]))
    
    while (g>np.array([epsilon,epsilon])).any():
        
        point=point-gamma*g
        g=np.array([grad_f[0](point[0],point[1]),grad_f[1](point[0],point[1])])
    return point

def one_step_grad_descent(grad_f,guess,gamma, epsilon):
    point=guess
    g=np.array(grad_f[0](point[0],point[1]),grad_f[1](point[0],point[1]))
    
    point=point-gamma*g
    return point

def gradient_2param(f):
    h=10**(-5)
    partial_x=lambda x,y:(f(x+h,y)-f(x,y))/h
    partial_y=lambda x,y:(f(x,y+h)-f(x,y))/h
    
    return np.array([partial_x,partial_y])

Q=lambda x,y:3*(x-2)**2+5*(y+1)**2

point=one_step_grad_descent(gradient_2param(Q),np.array([10,10]),0.1, 10**(-5))
min_x,min_y=point

x = np.linspace(-10, 10, 30)
y = np.linspace(-10, 10, 30)
X, Y = np.meshgrid(x, y)
Z = Q(X,Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

ax.scatter([min_x,2],[min_y,-1],[Q(min_x,min_y),Q(2,-1)], color=['red','blue'], s=100, label='(0,0,0)')

plt.show()