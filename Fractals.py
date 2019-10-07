#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:44:25 2019

@author: DannySwift
"""

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

m = 480
n = 320
 
s = 300  # Scale.
iterations=10
x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))
start_angle = np.radians(90)
angle = np.radians(120)
angles = [start_angle]
mid_xs = [0]
mid_ys = [0]
lines=[]
            
            
def animate(i, mid_xs, mid_ys, angles):
    bp = 3**i #branchpoints
    xs = mid_xs[-bp:]
    ys = mid_ys[-bp:]
    if i==0:
        lines.append(ax.plot([],[],lw=1, color='g')[0])
        lines[0].set_data([0,0], [0,1])
        mid_xs.append(0)
        mid_ys.append(0.5)
        angles.append(start_angle)
    bpangles = angles[-bp:]
    for k in range(bp):
        lines.append(ax.plot([],[],lw=1, color='g')[0])
        lines.append(ax.plot([],[],lw=1, color='g')[0])
        x, y = xs[k], ys[k]
        a = bpangles[k]
        a1 = a + angle 
        a2 = a - angle
        newx1, newy1 = x + np.cos(a1) / 2**i, y + np.sin(a1) / 2**i
        newx2, newy2 = x + np.cos(a2) / 2**i, y + np.sin(a2) / 2**i
        lines[-1].set_data([x, newx1], [y, newy1])
        lines[-2].set_data([x, newx2], [y, newy2])
        mid_xs.append(x + (np.cos(a) / 2**i) / 2)
        mid_xs.append((x + newx1) / 2)
        mid_xs.append((x + newx2) / 2)
        mid_ys.append(y + (np.sin(a) / 2**i) / 2)
        mid_ys.append((y + newy1) / 2)
        mid_ys.append((y + newy2) / 2)
        angles.append(a)
        angles.append(a1)
        angles.append(a2)
    
    return lines
            
        
        


if __name__ == '__main__':
    fig = plt.figure()
    #fig.set_size_inches(m / 100, n / 100)
    ax = plt.axes(xlim=(-1,1), ylim=(-1,1))
    ax.set_xticks([])
    ax.set_yticks([])
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    
    ani = animation.FuncAnimation(fig, animate, frames=iterations, fargs=(mid_xs, mid_ys, angles), interval=2000)
    plt.show()
    