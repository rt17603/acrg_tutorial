#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:28:44 2018

@author: rt17603
"""

import numpy as np
import xarray as xr
#import xarray as xray ## May sometimes see xarray import written as this, use xray.open_dataset in that case

filename = "data/AGAGE-GC-FID_MHD_19940101_ch4-10m.nc"
ds = xr.open_dataset(filename)

print("*** Observations dataset extracted from a netCDF file ***")
print(ds)

meas1 = ds.ch4

print("*** CH4 mol fraction data accessed using ds.key ***")
print(meas1)

meas2 = ds["ch4"]

print("*** CH4 mol fraction data accessed using ds[key] ***")
print(meas2)

meas = ds["ch4"].values

print("*** Extracted mol fraction value for ch4 ***")
print(meas)
print("Object type: ", type(meas))
print("Length: ", len(meas))
print("Shape: ", meas.shape)


print("*** Numpy operations: indexing and calculating the sum ***")
print(ds["ch4"].values[0:5])
print(np.sum(ds["ch4"].values))


time = ds['time']

print("*** Extracted time coordinates for CH4 ***")
print(time)
print("*** Extracted time coordinates values for CH4 ***")
print(time.values)
print("Object type: ", type(time))
print("Length: ", len(time))
print("Shape: ", time.shape)