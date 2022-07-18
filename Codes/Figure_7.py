#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:53:13 2022

@author: lviens
"""

import numpy as np
import scipy.io as sio
from scipy import stats
import matplotlib.pyplot as plt

#%%
dir_in = '../Data/' #  Data folder
dir_out = '../Figures/' # Output folder

fig = plt.figure(figsize = (14, 8))
fnt = 14
subidx = 1

stations = [2000, 3000, 4500, 5000] # List of virtual source channels
 
for station in stations : 
    
    dc_ma = sio.loadmat( dir_in + '/Figure_7_Station_' + str(station) + '.mat' ) # Load data
    freqDCpoints = np.squeeze(dc_ma['freqDCpoints']) # Load frequency of selected dispersion points
    phaseDCpoints = np.squeeze(dc_ma['phaseDCpoints'])# Load phase of selected dispersion points
    freqDCinv = np.squeeze(dc_ma['freqDCinv'])# Load frequency of inverted dispersion curve
    phaseDCinv = np.squeeze(dc_ma['phaseDCinv']) # Load phase of inverted dispersion curve
    VS = np.squeeze(dc_ma['VS']) # Load VS model
    
    
    # Plot dispersion curves
    ax0 = plt.subplot(2,len(stations), subidx)
    plt.plot(freqDCpoints, phaseDCpoints, '.', color = 'gray')
    for i in np.arange(len(phaseDCinv)):
        plt.plot(freqDCinv, phaseDCinv[i,:]*.001, 'k') # times 0.001 to have the phase velocity data in km/s
    plt.xlim(.5, 3)
    plt.ylim(0.25, 3)
    t1 = plt.title(str(station), fontsize = fnt )
    if subidx==1 :
        plt.ylabel('Phase velocity (km/s)', fontsize = fnt)
        plt.text(-.2, 3.05, '(a)', fontsize = fnt)
    else:
        ax0.set_yticklabels([])
    ax0.tick_params(bottom = True, top = True, left = True, right = True)
    plt.xlabel('Frequency (Hz)', fontsize = fnt)
    plt.xticks(fontsize = fnt)
    plt.yticks(fontsize = fnt)
    plt.grid()
    
    
    # Plot 1D velocity profile
    ax = plt.subplot(2, len(stations), subidx+len(stations))
    plt.plot(np.array(VS)*.001, np.arange(len(VS)), 'k', linewidth = 3)
    plt.xlim(0, 2.5)
    plt.ylim(1500, 0)
    plt.grid() 
    if subidx==1 :
        plt.ylabel('Depth (m)', fontsize = fnt)
        plt.text(-.7, -5, '(b)', fontsize = fnt)
    else:
        ax.set_yticklabels([])
    plt.xlabel('$V_S$ (km/s)', fontsize = fnt)
    plt.xticks(fontsize = fnt)
    plt.yticks(fontsize = fnt)
    ax.tick_params(bottom = True, top = True, left = True, right = True)
    subidx+=1
    
    # Fit the first 400 m of the VS model and plot
    depth_grad = 400 # in meters
    x = np.arange(depth_grad) 
    y = VS[:depth_grad]*.001
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    plt.plot(x*slope + intercept , x, linewidth = 3, color = 'dodgerblue')
    t= plt.text(1.2, 400, '$V_S$ gradient:\n    ' + str(np.round(slope*1000,2)) +' $s^{-1}$', fontsize = fnt, color = 'dodgerblue')
    t.set_bbox(dict(facecolor = 'white', alpha = 0.8, edgecolor = 'black', boxstyle = 'round'))
    
    
plt.tight_layout()
fig.savefig(dir_out + '/Figure_7.png', dpi=200)
