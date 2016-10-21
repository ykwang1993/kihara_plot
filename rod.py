
import matplotlib.pyplot as plt
from matplotlib import collections, transforms
from matplotlib.colors import colorConverter
import numpy as np

r = 1.
l = 2.

nverts = 50
theta = np.linspace(0,np.pi, nverts)
x_r_c = r * np.sin(theta)+l
y_r_c = r * np.cos(theta)

theta = np.linspace(-np.pi,0, nverts)
x_l_c = r * np.sin(theta)-l
y_l_c = r * np.cos(theta)

x = np.hstack((x_r_c,x_l_c)).reshape(-1,1)
y = np.hstack((y_r_c,y_l_c)).reshape(-1,1)

circle_pst = np.hstack((x,y))





plt.plot(circle_pst[:,0],circle_pst[:,1])
plt.show()