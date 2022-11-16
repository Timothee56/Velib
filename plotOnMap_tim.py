#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:02:16 2022

@author: timotheerigagneau
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

positions = [
    [2.275725,2.3360354080796,2.3433353751898,2.366104461987773,2.315508019010038],
    [48.865983,48.837525839067,48.85165383178419,48.85165383178419,8.91039875761846]
    ]

BBox = ((1.9933,   2.7349,      
         48.6420, 49.0554))
"""       
BBox = ((df.longitude.min(),   df.longitude.max(),      
         df.latitude.min(), df.latitude.max())
"""

ruh_m = plt.imread('/Users/timotheerigagneau/Documents/ENPC/S1/Nouvelles_donnees/Images/Fond de plan/Image de fond.png')

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(positions[0], positions[1], zorder=1, alpha= 0.5, c='b', s=20)
ax.set_title('Plotting Spatial Data on Riyadh Map')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')

"""

How to plot coordonate on a map image : 
https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db

"""