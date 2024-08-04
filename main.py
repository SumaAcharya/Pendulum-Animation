import  numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as anm

def pendulum_motion(X,t):

    m= 2
    g=9.81
    b=0.15
    l=1

    theta=X[0]
    dtheta=X[1]
    d2theta= -(b/m)*dtheta-(g/l)*np.sin(theta)

    return [dtheta,d2theta]

X0 = [np.pi/3,0]
time_step=0.01
time= np.arange(0,10+time_step,time_step)
soln= odeint(pendulum_motion,X0,time)

theta= soln[:,0]
L= 1
x= L*np.sin(theta)
y= -L*np.cos(theta)

pend_fig = plt.figure()
ax = pend_fig.add_subplot()
ax.set_xlim(-L,L)
ax.set_ylim(-1.25*L,0.25)

line, = ax.plot([],[])
def pend_anim(i):
    xp =(0,x[i])
    yp =(0,y[i])
    line.set_xdata(xp)
    line.set_ydata(yp)

    return line
anim = anm.FuncAnimation(pend_fig,pend_anim,frames=len(soln),interval=0.01)

plt.show()

plt.plot(time,theta*180/np.pi)
plt.show()


