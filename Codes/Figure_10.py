#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:24:27 2022

@author: lviens
"""

import numpy as np
import scipy.io as sio
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import MultipleLocator


dir_in = '../Data/'
dir_out  = '../Figures/'

file1 = dir_in + '/Data_Figure_10a.mat'
data = sio.loadmat(file1) 
extenteq = np.squeeze( data['extent'])
Strain_data = np.squeeze( data['Strain_data'])

file2 = dir_in + '/Data_Figure_10b_velocity_model.mat'
data = sio.loadmat(file2) 
extentVS = np.squeeze( data['extent'])
VS = np.squeeze( data['VS'])

#%%
fnt = 18
colormapvs2 = []
colormapvs2 = cm.get_cmap('magma_r', 2000) #cm.magma_r #viridis_r #cm.viridis_r
colormapvs2.colors[0] = [0,1,1,1]
 

f2= plt.figure(figsize =(14,10))
 
cl = 1.9*10**-8

ax1=f2.add_subplot(211)
plt.imshow(Strain_data.T, aspect = 'auto',  clim = (-cl, cl), cmap = 'bone' , extent = (extenteq[0] , extenteq[1],  extenteq[2], extenteq[3] ) )
ax1.tick_params(bottom=True, top=True, left=True, right=True)
plt.text(1200, 8, '(a)', fontsize = fnt)

plt.text(2000, 13, 'P-wave', weight='bold', fontsize = 14)
plt.plot([2200,2350 ] , [14,15], 'k')
plt.text(3100, 23.5, 'S-wave',  weight='bold', fontsize = 14)
plt.plot([3300,3450 ] , [ 24.5, 25.5], 'k')
plt.ylabel('Time (s)', fontsize = fnt)
ax1.yaxis.set_minor_locator(MultipleLocator(5))

plt.text(4480, 29.75, 'SW',weight='bold', fontsize = 14)
xy = [4580, 30.5]
plt.plot([xy[0],xy[0] + 150 ] , [ xy[1], xy[1] + 1.5], 'k' , lw = 2)

plt.text(2550, 29.75, 'SW',weight='bold', fontsize = 14)
xy = [2500, 30.5]
plt.plot([xy[0],xy[0] + 150 ] , [ xy[1] + 1.5, xy[1]], 'k' , lw = 2)

ax1.annotate('', xy=(2100, 25.5),xytext=(2100, 22), va='center',ha='center'  , arrowprops={ 'lw': 2, 'facecolor': 'r'})

ax1.annotate('', xy=(5300, 25.5),xytext=(5300, 22), va='center',ha='center'  , arrowprops={ 'lw': 2, 'facecolor': 'r'}) #'arrowstyle': '->',



plt.xlim(1750 , 8120)
plt.xticks(fontsize=fnt )
plt.yticks(fontsize=fnt )
dx = 5.1
dtmt = np.arange(2000*dx/1000,8001*dx/1000, 1000*dx/1000 )
ax1b = ax1.twiny()
ax1b.set_xlim(extenteq[0]*dx/1000 ,extenteq[1]*dx/1000)
plt.xlabel('Distance to the coast (km)', fontsize =fnt)
ax1b.set_xticks(dtmt)
ax1.set_xticklabels([])
plt.xticks(fontsize = fnt)
plt.grid(linewidth = .2)


# Plot colorbar
rect = plt.Rectangle( (7350, 46) ,  1000, 13, alpha = .75, facecolor = 'w', edgecolor = 'k',  zorder = 1 )
ax1.add_patch(rect)
cbaxes = f2.add_axes([0.865, 0.5575, 0.07, 0.015])
cb = plt.colorbar( cax = cbaxes,orientation = 'horizontal'  ) 
cb.ax.set_title('Strain', fontsize=fnt-2) 



ax2=f2.add_subplot(212)
im = plt.imshow(VS, aspect = 'auto', cmap = colormapvs2, clim = ( 0, 2000), extent = (extentVS[0]  , extentVS[1] , extentVS[2],extentVS[3] ) )
ax2.tick_params(bottom=True, top=True, left=True, right=True)
plt.text(1200, 0, '(b)', fontsize = fnt)

plt.xlim(1750 , 8120)
plt.ylim(1200, 0)
plt.ylabel('Depth (m)', fontsize=fnt)
plt.xlabel('Channel #',fontsize=fnt)
plt.grid(linewidth = .2)
plt.xticks(fontsize=fnt )
plt.yticks(fontsize=fnt )
ax2.annotate('', xy=(2100, 140),xytext=(2100, 50), va='center',ha='center'  , arrowprops={ 'lw': 2, 'facecolor': 'r'}) # 
ax2.annotate('', xy=(5300, 480),xytext=(5300, 390), va='center',ha='center'  , arrowprops={ 'lw': 2, 'facecolor': 'r'}) #'arrowstyle': '->',


# Create a Rectangle patch
rect = patches.Rectangle((7000, 100), 1000, 500,   edgecolor='k', facecolor='w', alpha = .7)

# Add the patch to the Axes
ax2.add_patch(rect)
pos = f2.add_axes([0.82, 0.3, 0.025,0.12]) 
cb2  = plt.colorbar(im, cax = pos,  shrink=0.5, aspect = 10 )
plt.yticks(fontsize = fnt)
cb2.ax.set_title('$V_S$', fontsize =fnt)
cb2.ax.set_ylabel('m/s', fontsize =fnt)

ax1.set_position([.1, .514  , .85, .428])
ax2.set_position([.1, .065 , .85, .428])
f2.savefig(dir_out + '/Figure_10.png', dpi=200)
