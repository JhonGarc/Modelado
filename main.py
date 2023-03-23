import numpy as np
import matplotlib.pyplot as plt


Asimulacion=[1,2,3,4,5]
x0 = 3.9
tstart=0
tstop=5
increment=0.1

t = np.arange(tstart, tstop+1, increment)
x=np.zeros(tstop+1)

for k in Asimulacion:
    x = np.exp(k*t)*x0
    plt.plot(t,x)


plt.title('Crecimiento exponencial')
plt.xlabel('tiempo')
plt.ylabel('x(t)')

plt.axis([0,5,0,100])
plt.show()