#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:12:24 2018

@author: rt17603
"""

import matplotlib.pyplot as plt
import numpy as np
import cartopy

x = np.arange(-180,180,5)
y = np.arange(-90,90,5)
xx, yy = np.meshgrid(x,y)
z = np.sin( ((xx//40.0) + (yy//40.0)) % 2 )

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(1,2,1, projection=cartopy.crs.PlateCarree())

ax1.add_feature(cartopy.feature.BORDERS, linestyle=':')
ax1.coastlines()
ax1.contourf(xx, yy, z, 15, cmap="bwr", vmin=-1.0, vmax=2.0)
ax1.set_title("Plate Carree")

ax2 = fig.add_subplot(1,2,2, projection=cartopy.crs.Geostationary())

ax2.add_feature(cartopy.feature.BORDERS, linestyle=':')
ax2.coastlines()
ax2.contourf(xx, yy, z, 15, cmap="bwr", transform=cartopy.crs.PlateCarree(), vmin=-1.0, vmax=2.0)
ax2.set_title("View from a satellite")

plt.show()