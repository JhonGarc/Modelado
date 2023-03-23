import numpy as np
import matplotlib.pyplot as plt


Asimulacion=[1,2,3,4,5]
n = 10
x0 = 1
tstart=0
tstop=5
increment=0.1

t = np.arange(tstart, tstop+1, increment)
x=np.zeros(tstop+1)

for k in Asimulacion:
    x = (n * (x0*np.exp(k*t))) / (n - x0 + x0 * np.exp(k*t))
    plt.plot(t,x)


plt.title('crecimiento logistico')
plt.xlabel('tiempo')
plt.ylabel('x(t)')

plt.axis([0,5,0,20])
plt.show()