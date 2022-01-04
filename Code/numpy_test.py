import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
dims = [4096] * 7
print(dims, dims[0])
hs = []
#print(np.random.randn())

s = np.random.poisson(5, 10000)
#count, bins, ignored = plt.hist(s, 14, density=True)
#print(s, s.shape)
#plt.show()
x = np.random.randn(16, dims[0])
print('x_init>>', x.shape)
if 0:
#for Din, Dout in zip(dims[:-1], dims[1:]):
        print('Din, Dout >> ', Din, Dout)
        W = 0.01 * np.random.randn(Din, Dout)
        #print(W, W.shape)
        #print(W.shape, x.dot(W).shape)
        x = np.tanh(x.dot(W))
        hs.append(x)
        print(x.shape)
print(len(hs), x.shape)

#def batchnorm_forward(x, gamma, beta, eps=1e-5):
def batchnorm_forward(x, gamma=1, beta=0, eps=1e-5):
    N, D = x.shape
        
    sample_mean = x.mean(axis=0)
    sample_var = x.var(axis=0)
    print(sample_mean,sample_var)
    print(sample_mean.shape,sample_var.shape)
    
    std = np.sqrt(sample_var + eps)
    x_centered = x - sample_mean
    x_norm = x_centered / std
    out = gamma * x_norm + beta
    
    cache = (x_norm, x_centered, std, gamma)

    return out, cache
batchnorm_forward(x)











if 0:
    x = np.arange(-10, 10, 0.025)
    print(x.shape)
    #plt.plot(x,(1-np.exp(-2*x))/(1+np.exp(-2*x)))
    plt.plot(x,np.tanh(x))
    plt.title("y = (1-exp(-2x))/(1+exp(-2x))")
    plt.show()


