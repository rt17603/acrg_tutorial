#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:11:55 2018

@author: rt17603
"""

import matplotlib.pyplot as plt
import cartopy

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection=cartopy.crs.PlateCarree())

ax.add_feature(cartopy.feature.BORDERS, linestyle=':')
ax.coastlines(resolution="50m")

ax.set_extent([-15,10,45,60])

ax.scatter(-2.58, 51.45, label= "Bristol", s=100)
ax.scatter(-9.90, 53.33, label= "Macehead", s=100)
ax.legend()

plt.show()