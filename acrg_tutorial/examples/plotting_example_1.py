#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:09:01 2018

@author: rt17603
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/ch4_macehead_2014.csv", parse_dates = ["time"])

print(df)

plt.plot(df.time, df.mf)
plt.show()