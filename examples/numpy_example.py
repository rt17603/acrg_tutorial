#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:04:01 2018

@author: rt17603
"""

import numpy as np

print(np.sqrt(9.))

arr = np.array([1.,1.,2.,3.,5.,8.])

print(arr * 2)

print(arr[2] * 2)

print(arr[0:3])

print(np.sum(arr))

arr[0] = 0.
print(arr[0])

ch4array = np.genfromtxt('data/ch4_macehead_2014.csv', delimiter=',', skip_header=1)

print ch4array[0:10,:]

print ch4array[:,1]