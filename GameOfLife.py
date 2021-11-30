# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:26:21 2021

@author: jerem
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import product
import time

ratio = 3

SIZE = (int(10*ratio), int(10*ratio))
X,Y = SIZE
M = np.zeros(SIZE)


# M[9,8] = 1
# M[9,10] = 1
# M[10,8] = 1
# M[10,10] = 1
# M[8,9] = 1
# M[11,9] = 1
# M[11,10] = 1

fig, ax = plt.subplots()

img = ax.imshow(M, origin = "lower", cmap = "gray_r")
ax.set_xticks(np.arange(-.5, X, 1))
ax.set_yticks(np.arange(-.5, Y, 1))
ax.set_xticklabels(np.arange(0, X, 1))
ax.set_yticklabels(np.arange(0, Y, 1))
ax.grid(color='b', linewidth=0.5)


def neighbours(x,y,M):
    sizeX = SIZE[0]
    sizeY = SIZE[1]
    TOP = [M[(y - 1)%sizeY, (x + k)%sizeX] for k in range(-1,2)]
    MID = [M[y, (x + k)%sizeX] for k in [-1,1]]
    BOT = [M[(y + 1)%sizeY, (x + k)%sizeX] for k in range(-1,2)]

    count = sum(TOP) + sum(MID) + sum(BOT)

    return count

def onAction(event):
    global newM
    if event.xdata is None or event.ydata is None: return
    x,y = event.xdata + 0.5, event.ydata + 0.5

    xint, yint = int(x), int(y)
    newM[yint,xint] = (M[yint,xint] + 1)%2
    print("ACTION", xint,yint)

fig.canvas.mpl_connect('button_press_event', onAction)

import keyboard

newM = np.copy(M)
PAUSE = True
for t in range(100000):
    t0 = time.perf_counter()
    plt.pause(0.01)
    print("\n -----", t, "----------------------")
    if keyboard.is_pressed('space'):
        PAUSE = not PAUSE
        print("==============================")

    # print(M)
    # print("new",newM)

    for x in range(SIZE[0]):
        if PAUSE: continue

        for y in range(SIZE[1]):
            current_cell = M[y,x]
            count = neighbours(x,y,M)
            if count < 2 or count > 3:
                newM[y,x] = 0 #KILL
            if current_cell == 0 and count == 3:
                newM[y,x] = 1 #BIRTH
    # print(M)
    # print("new",newM)
    t
    # print(newM)

    img.set_data(newM)
    M = np.copy(newM)
    img.autoscale()
    ax.grid(color='gray', linewidth=0.5)
    tend = time.perf_counter()
    print("pause:",PAUSE)
    print(round((tend - t0)*1000,2),"ms")




