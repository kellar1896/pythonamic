import numpy as np  
import matplotlib.pyplot as plt


theta = np.arange(0,  2*np.pi, 0.01)
theta1 = np.arange(0, 360, 1)
#E = np.real( 1 * np.sin(theta))
E = abs(12*np.cos(3*theta-(np.pi/7))*np.sin(2*theta))
#E1 = abs(np.real(45/2*np.cos((5*np.pi/2)*np.cos(theta))/np.sin(theta)))
#E2 = abs(np.real(45/3*np.cos((5*np.pi/2)*np.cos(theta))/np.sin(theta)))
#E3 = abs(np.real(45/10*np.cos((5*np.pi/2)*np.cos(theta))/np.sin(theta)))
Emax = np.max(E)
print("caida a -3 dB desde el punto max")
print(Emax*0.707)

 
plt.figure(1)    
ax = plt.subplot(131, polar=True)
ax.plot(theta, E)
#bx = plt.subplot(131, polar=True)
#bx.plot(theta, E1)
#cx = plt.subplot(131, polar=True)
#cx.plot(theta, E2)
#dx = plt.subplot(131, polar=True)
#dx.plot(theta, E3)



bx = plt.subplot(122)
bx.plot(theta * 360 /(2*np.pi), E)
plt.show()
