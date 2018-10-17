#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:10:19 2018

@author: rt17603
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/ch4_macehead_2014.csv", parse_dates = ["time"])

fig = plt.figure(figsize=[12,5])
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(df.time, df.mf)
ax2.plot(df.time, df.mf)

x_min = pd.to_datetime("2014-01-01", format="%Y-%m-%d")
x_max = pd.to_datetime("2014-02-01", format="%Y-%m-%d")

ax1.axvspan(x_min, x_max, alpha=0.5, color="red")
ax2.set_xlim([x_min, x_max])
plt.show()