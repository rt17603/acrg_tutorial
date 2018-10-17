#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:11:12 2018

@author: rt17603
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-np.pi,np.pi,0.1)
y = np.arange(-np.pi,np.pi,0.1)
xx, yy = np.meshgrid(x,y)
z = np.cos(xx) + np.cos(4 * yy)

plt.contourf(xx, yy, z, 25)
plt.show()