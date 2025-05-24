import numpy as np

A=np.array([[2,1,3],[15,2,0],[1,3,1]])+0.0

def Gaussian(M, b, epsilon=1e-5):
    assert M.shape[0]==M.shape[1]

    b=b.reshape(1,-1)
    Aug=np.hstack((M,b.T))
    n,m=Aug.shape

    for k in range(n-1):
        m_i=np.argmax(Aug[:,k]) # maximal index
        if np.abs(Aug[m_i,k]) < epsilon:
            raise BaseException("The matrix is singular")
        
        Aug[[k,m_i]]=Aug[[m_i,k]]
        
        pivot=Aug[k,k]
        Aug[k:,:]-=Aug[k,:]*Aug[k+1,k]/pivot

        Aug[Aug<epsilon]=0

    return Aug[:,:Aug.shape[1]-1],Aug[:,-1]

b=np.array([10,5,3])+0.0
Gaussian(A,b)