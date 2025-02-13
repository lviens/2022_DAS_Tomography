#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:11:47 2021

@author: lviens
"""

import h5py
import numpy as np
import matplotlib.colors
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from matplotlib.ticker import (MultipleLocator)
from matplotlib.colors import LinearSegmentedColormap

cm_data = [[0.2081, 0.1663, 0.5292], [0.2116238095, 0.1897809524, 0.5776761905], [0.212252381, 0.2137714286, 0.6269714286], 
           [0.2081, 0.2386, 0.6770857143],  [0.1959047619, 0.2644571429, 0.7279], [0.1707285714, 0.2919380952,   0.779247619], 
           [0.1252714286, 0.3242428571, 0.8302714286],  [0.0591333333, 0.3598333333, 0.8683333333], [0.0116952381, 0.3875095238, 0.8819571429],
           [0.0059571429, 0.4086142857, 0.8828428571], [0.0165142857, 0.4266, 0.8786333333], [0.032852381, 0.4430428571,   0.8719571429],
           [0.0498142857, 0.4585714286, 0.8640571429],  [0.0629333333, 0.4736904762, 0.8554380952], [0.0722666667, 0.4886666667,   0.8467],
           [0.0779428571, 0.5039857143, 0.8383714286],  [0.079347619, 0.5200238095, 0.8311809524], [0.0749428571, 0.5375428571,   0.8262714286], 
           [0.0640571429, 0.5569857143, 0.8239571429],  [0.0487714286, 0.5772238095, 0.8228285714], [0.0343428571, 0.5965809524,   0.819852381], 
           [0.0265, 0.6137, 0.8135], [0.0238904762, 0.6286619048,  0.8037619048], [0.0230904762, 0.6417857143, 0.7912666667], 
           [0.0227714286, 0.6534857143, 0.7767571429], [0.0266619048, 0.6641952381,  0.7607190476], [0.0383714286, 0.6742714286, 0.743552381],
           [0.0589714286, 0.6837571429, 0.7253857143], [0.0843, 0.6928333333, 0.7061666667], [0.1132952381, 0.7015, 0.6858571429], 
           [0.1452714286, 0.7097571429, 0.6646285714], [0.1801333333, 0.7176571429,   0.6424333333], [0.2178285714, 0.7250428571, 0.6192619048], 
           [0.2586428571, 0.7317142857, 0.5954285714], [0.3021714286, 0.7376047619,   0.5711857143], [0.3481666667, 0.7424333333, 0.5472666667], 
           [0.3952571429, 0.7459, 0.5244428571], [0.4420095238, 0.7480809524,  0.5033142857], [0.4871238095, 0.7490619048, 0.4839761905], 
           [0.5300285714, 0.7491142857, 0.4661142857], [0.5708571429, 0.7485190476,  0.4493904762], [0.609852381, 0.7473142857, 0.4336857143], 
           [0.6473, 0.7456, 0.4188], [0.6834190476, 0.7434761905, 0.4044333333],  [0.7184095238, 0.7411333333, 0.3904761905], 
           [0.7524857143, 0.7384, 0.3768142857], [0.7858428571, 0.7355666667,   0.3632714286], [0.8185047619, 0.7327333333, 0.3497904762], 
           [0.8506571429, 0.7299, 0.3360285714], [0.8824333333, 0.7274333333, 0.3217], [0.9139333333, 0.7257857143, 0.3062761905],
           [0.9449571429, 0.7261142857,  0.2886428571], [0.9738952381, 0.7313952381, 0.266647619],  [0.9937714286, 0.7454571429, 0.240347619],
           [0.9990428571, 0.7653142857,  0.2164142857], [0.9955333333, 0.7860571429, 0.196652381],  [0.988, 0.8066, 0.1793666667],
           [0.9788571429, 0.8271428571, 0.1633142857],  [0.9697, 0.8481380952, 0.147452381], [0.9625857143, 0.8705142857, 0.1309], 
           [0.9588714286, 0.8949, 0.1132428571], [0.9598238095, 0.9218333333,   0.0948380952], [0.9661, 0.9514428571, 0.0755333333], 
           [0.9763, 0.9831, 0.0538]]

parula_map = LinearSegmentedColormap.from_list('parula', cm_data)
test_cm = parula_map

def get_frequencydomain_info(data, dt = 0.1, lfhf = [0.1, 4]):
        """
        Parameters
        ----------
        data : 2D Array
            Array of data.
        dt : float, optional
            Sampling rate in seconds. The default is 0.1 s.
        lfhf : List
            List containing the two cutoff frequencies in Hz. The default is 0.1 and 4 Hz
    
        Returns
        -------
        freqpoints: Frequency axis.
        cumphase: Unwraped phase of the data.
        """

        num_ts = data.shape[1]
        data -= data.mean() # remove mean of the data
        
        fs = np.fft.fftfreq(num_ts,dt) # frequency 
        fd_data = np.fft.rfft(data) # fft of the data
        fs_positive = fs[:fd_data.shape[1]]
        if num_ts%2==0:
            fs_positive[-1] = -1*fs_positive[-1]
        # Even number of samples: the last value returned by rfft is the Nyquist freq.
        # Odd number of samples: last value is fftfreq is the negative Nyquist frequency
        rel_indices=np.intersect1d(np.where(fs_positive>=lfhf[0])[0],np.where(fs_positive<=lfhf[1])[0])
        freq_points = fs_positive[rel_indices]
        afdm = np.matrix(fd_data[:,rel_indices])
        unwraped_phase=np.unwrap(np.angle(afdm))
        return freq_points, unwraped_phase

def do_single_freq(distance, true_phase_data, ktrials):
    """
    Parameters
    ----------
    absdist : TYPE
        List of distances (in km).
    true_phase : TYPE
        True phase of the data.
    ktrials : TYPE
        

    Returns
    -------
    mod_stack : TYPE
        Dispersion Image
    """
    relative_dist = distance - distance[0]
    kxmat = np.outer(ktrials, relative_dist)
    apsm = np.exp(+1j*kxmat) # Applied phase shift matrix
    tpmat = true_phase_data.reshape(len(true_phase_data),1)
    tpcm = np.exp(1j*tpmat) #True phase column matrix
    stacked_mats = np.dot(apsm,tpcm)
    mod_stack = np.abs(stacked_mats)
    return mod_stack


def butter_bandpass_filter(data, lowcut, highcut, fs, order=4):
    # Butterworth bandpass filter
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y

def maxlocal(y):
    # Function do get local maxima
    maxloc = []
    indmax = []
    maxloc.append(y[0])
    indmax.append(0)
    for i in np.arange(1,len(y)-1):
        if y[i]>y[i-1] and y[i]>=y[i+1]:
          maxloc.append(y[i])
          indmax.append(i)
    return maxloc,indmax

#%% Changeable parameters

dir_in = '../Data'  # input directory with the CCF files
dir_out = '../Figures'#   Output directory


station = 4000
station_selection = 400 # change this to select more or less stations 
    

# Parameters for the slant-stack
f1 = .25 # low-cut frequency (in Hz)
f2 = 5  # high-cut frequency (in Hz)
 
cmin = 0.05 # Min Phase vel. (in km/s)
cmax = 3 # Max Phase vel. (in km/s)
step = 0.001 # step for the phase vel. (in km/s). 0.002 km/s-> 2 m/s



#%% The following parameters should not be changed
spatial_samp = 0.0051 # Station spacing is 5 m 
middle_station = 0
delta = 10 # Sampling frequency in Hz
c_vect=np.arange(cmin,cmax+step,step)
frange = [f1, f2] #  frequency range of interest (Hz)

#%% read data
file = dir_in  + '/Figure_2_Virt_' + str(station).zfill(4) + '.hdf5'
f = h5py.File(file, 'r')
das = np.array(f['DAS'][:])

dasf = []
for df in range(len(das)):
    dasf.append(butter_bandpass_filter(das[df], lowcut=f1, highcut=f2-.001, fs = delta, order=4) ) 
        
dasf/= np.max(np.abs(dasf)) # normalize the data
t = np.linspace(-len(dasf[0])/2/delta ,len(dasf[0])/2/delta -1/delta, len(dasf[0])) 

  

#%% Select data 
staini = station  
data3 = (dasf[:station_selection, int(dasf.shape[1]/2):])
data = data3[:,:int(80*delta)]
epdist = np.arange(0, (station_selection)*spatial_samp, spatial_samp) 
   

#%% Compute slant-stack
dt = 1/delta
freqpoints, cumphase = get_frequencydomain_info(data, dt, frange)

specraw=np.zeros((c_vect.size,len(freqpoints)))
for j in range(len(freqpoints)):
	ktry=(2*np.pi*freqpoints[j])/c_vect  
	stack_thisfreq = do_single_freq(epdist,cumphase[:,j],ktry)
	specraw[:,j] = stack_thisfreq[:,0]
spec_norm = specraw/np.max(specraw,0)
X,Y = np.meshgrid(freqpoints, c_vect)

#%% Select dispersion points
Aplot= spec_norm
fplot = X
cplot = Y

c=cplot[:,0]
ic0=np.argwhere(c>.3)[0] 
nc=len(c)
f=fplot[0,:]
rayf=[]
rayDC=[]
rayf2 = []
rayDC2 = []
for j in np.arange(len(Aplot[0]) ):
    maxloc,indmax=maxlocal(Aplot[:,j])
    ic0 = np.argwhere(c>(.25+(f[j]-1)*.025))[0]  
    keep = np.squeeze(np.array(indmax)[indmax>ic0]  )
    if keep.size>0:
        rayf2.append(f[j]*np.ones(keep.size) )
        rayDC2.append(c[keep])
        
        
#%% Plot the data
fnt = 14
cl = .005
xl = 25

fig = plt.figure(figsize=(9,12))

ax = plt.subplot(211) # plot CCFs
plt.imshow(dasf,aspect = 'auto',clim = (-cl, cl) , extent =( t[0], t[-1],station + len(dasf) ,station  ) )
plt.grid(linewidth = .25)

plt.xlim(-xl,xl)
plt.ylim(station+station_selection,station)
plt.xlabel('Time (s)', fontsize = fnt)
plt.ylabel('Channel #', fontsize = fnt)
plt.title('CCFs - Virtual source ' + str(station) + '\n Bandpass filter: ' + str(f1) +'-' + str(f2) +' Hz',fontsize = fnt)

x = np.linspace(-25, 25, 1000)
y = 500*x/5
plt.plot(x,y+station,'--', color = 'red', linewidth = 2)
plt.text (.5,station+station_selection-20,'500 m/s', color = 'red', rotation=-84, fontsize = fnt)
plt.text(-31, station - 15, '(a)', fontsize = fnt+2)

ax.tick_params(bottom=True, top=True, left=True, right=True)
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(5))
plt.yticks(fontsize = fnt)
plt.xticks(fontsize = fnt)

dtmt = np.round(np.linspace((station-200)*spatial_samp,(station+200)*spatial_samp, 11) ,1)
ax1b = ax.twinx()
ax1b.set_ylim(dtmt[0], dtmt[-1])
plt.yticks(dtmt ,fontsize = fnt)
ax1b.invert_yaxis()
ax1b.set_ylabel('Distance to the coast [km]',fontsize = fnt)


ax1=fig.add_subplot(212) # plot dispersion image
plt.text(-.3, 3, '(b)', fontsize = fnt+2)
sm = plt.contourf(fplot,cplot, Aplot, 10, cmap = parula_map , vmin = 0 , vmax = 1)
plt.yticks(fontsize = fnt)
plt.xticks(fontsize = fnt)
plt.ylim(.25, 3)
plt.xlabel('Frequency (Hz)', fontsize = fnt)
plt.ylabel('Phase velocity (km/s)', fontsize = fnt)
norm= matplotlib.colors.Normalize(vmin=0, vmax=1.001)

sm2 = plt.cm.ScalarMappable(norm=norm, cmap = sm.cmap)
sm2.set_array([])
colorbar_ax = fig.add_axes([0.9, 0.2, 0.018, 0.15])
cb2 =fig.colorbar(sm2, cax=colorbar_ax, ticks=np.arange(0,1.01,.2) )
cb2.ax.set_ylabel('Norm. amplitude\n  ', fontsize = fnt)
plt.yticks(fontsize = fnt)


for i in np.arange(len(rayf2)): # plot dispersion points
    ax1.scatter(rayf2[i],rayDC2[i] , s = 1, color = 'k' )

ax1.tick_params(bottom=True, top=True, left=True, right=True)
plt.grid(linewidth = .25)
ax1.xaxis.set_minor_locator(MultipleLocator(.1))
ax1.yaxis.set_minor_locator(MultipleLocator(.1))
ax1.xaxis.set_major_locator(MultipleLocator(.5))

ax.set_position([0.1, .54, .79, .41])
ax1.set_position([0.1, .06, .79, .41])
plt.show()
fig.savefig(dir_out + '/Figure_2.png', dpi=300)
plt.close()

