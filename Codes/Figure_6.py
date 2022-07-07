#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 13:44:16 2022

@author: lviens
"""
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

#%% Data and Figure folders

dir_in = '../Data/'
dir_out = '../Figures'

fnt = 14
fig = plt.figure(figsize = (10, 8))
#%% Load and plot velocity profiles (Figure 6a)
sub1 = plt.subplot(221)
file = dir_in + '/Fig6_a_data.mat'
b = sio.loadmat(file)
data = np.squeeze(b['datafin'])
xa = np.squeeze(data['x']).tolist()
ya = np.squeeze(data['y']).tolist()

plt.plot( np.squeeze(xa[0]).tolist()[0]/1000 ,  np.squeeze(ya[0]).tolist()[0]/1000 ,'b', linewidth = 3)
plt.plot( np.squeeze(xa[2]).tolist()[0]/1000 , np.squeeze(ya[2]).tolist()[0]/1000 , 'k', linewidth = 3)
plt.xlim( 0, 4)
plt.ylim(4, 0)
plt.grid()
plt.xticks(fontsize =fnt)
plt.yticks(fontsize =fnt)
plt.xlabel('$V_S$ (km/s)', fontsize = fnt)
plt.ylabel('Depth (km)', fontsize = fnt)
plt.text(-1.5, 0.025 , '(a)', fontsize = fnt)
sub1.tick_params(bottom=True, top=True, left=True, right=True)

sub1.text(.2, 2.87, r'$\dfrac{\partial V_{S}}{\partial z}= 1\ s^{-1}$', color='k', fontsize=16 )
sub1.text(1.4, .5, r'$\dfrac{\partial V_{S}}{\partial z}= 2 \ s^{-1}$', color='b', fontsize=16 )

#%%Load and plot dispersion curves (Figure 6b)

sub2 = plt.subplot(222)
file =dir_in +  '/Fig6_b_data.mat'
b = sio.loadmat(file)
data = np.squeeze(b['datafin'])
xb = np.squeeze(data['x']).tolist()
yb = np.squeeze(data['y']).tolist()

for i in np.arange(50):
    plt.plot(np.squeeze(xb[i]).tolist()[0] , np.squeeze(yb[i]).tolist()[0] ,'b', linewidth =2)
for i in np.arange(100,150 ):
    plt.plot(np.squeeze(xb[i]).tolist()[0] , np.squeeze(yb[i]).tolist()[0] ,':k', linewidth = 2)
plt.xlim(0.5, 2.9)
plt.xticks(fontsize =fnt)
plt.yticks(fontsize =fnt)
plt.ylim(.2,4.25)
plt.grid()
plt.text(.2, 4.2 , '(b)', fontsize = fnt)
sub2.tick_params(bottom=True, top=True, left=True, right=True)
plt.ylabel('Phase velocity (km/s)',fontsize =fnt)

#%% Load and plot dispersion image for a step gradient of 1 s^-1 (Figure 6c)
sub3 = plt.subplot(223)
file =dir_in + 'Fig6_c_data.mat'
ddepth = sio.loadmat(file)
data = np.squeeze(ddepth['datafin'])
x = np.squeeze(data['x']).tolist()
y = np.squeeze(data['y']).tolist()
z = np.squeeze(np.squeeze(data['z'])).tolist()
z = z- np.nanmin(z)
z = z/np.nanmax(z)


freqlim = [np.squeeze(x[-1]).tolist()[0][0] , np.squeeze(x[-1]).tolist()[0][-1]]
vellim = [np.squeeze(y[-1]).tolist()[0][0] , np.squeeze(y[-1]).tolist()[0][-1]]
sm2  = plt.imshow(np.flipud((z) )  , extent = (freqlim[0] , freqlim[1] , vellim[0], vellim[1] ) ,aspect = 'auto' ,cmap = 'bone' , clim = (0,.7)) 
for i in np.arange(len(x)-1  ):
    plt.plot(np.squeeze(x[i]).tolist()[0] , np.squeeze(y[i]).tolist()[0] ,'k', linewidth = 1)
plt.xlim(0.5, 2.9)
plt.grid(lw = .5)
plt.ylim(.2,4.25)
plt.xlabel('Frequency (Hz)',fontsize =fnt)
plt.ylabel('Phase velocity (km/s)',fontsize =fnt)
plt.xticks(fontsize =fnt)
plt.yticks(fontsize =fnt)
plt.text(0.2, 4.2 , '(c)', fontsize = fnt)
sub3.tick_params(bottom=True, top=True, left=True, right=True)

plt.text( -.54 , .6, 'Normalised\n amplitude' ,fontsize = fnt)

colorbar_ax = fig.add_axes([0.15, 0.2, 0.03, 0.2])
cb3 = fig.colorbar(sm2, cax=colorbar_ax ,orientation='vertical') 
plt.yticks(fontsize = fnt)

#%%
sub1.set_position([.075, .53  , .2,.4])
sub2.set_position([.38, .53 , .6,.4])
sub3.set_position([.38, .08 , .6,.4])

fig.savefig(dir_out + '/Figure_6.png', dpi=200)
