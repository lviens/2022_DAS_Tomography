# Python codes to reproduce the results of Understanding surface-wave modal content for high-resolution imaging of submarine sediments with Distributed Acoustic Sensing

The codes are for the following manuscript:
- Viens L., M. Perton, Z. J. Spica, K. Nishida, T. Yamada, S. Shinohara, Understanding surface-wave modal content for high-resolution imaging of submarine sediments with Distributed Acoustic Sensing ([Preprint link](https://eartharxiv.org/repository/view/3266/))

## Description:
* The **Codes** folder contains:

  - **Figure_2.py** to reproduce Figure 2 of the paper (CCFs and compute slant-stack)
  - **Figure_3.py** to reproduce Figure 3 (compare CCFs computed with and without applying 1-bit normalization to the continuous noise data)


* The **Data** folder contains:
  - The data to reproduce Figures 2-4.
  

* The **Figures** folder contains 6 figures that can be plotted with the 4 codes. 


## Codes and their outputs:

* The **Figure_2.py** code reads the CCFs computed using channel 4000 as the virtual source. 
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Tomography
/blob/main/Figures/Figure_2.png" width=75%/>
</p>
<br/>
<br/>

* The **Reproduce_Fig_2.py** code shows theACFs computed from the 103 earthquakes bandpass filtered between 10 and 20 Hz at channels (a) 5000 and (b) 7000. (c--d) Same as (a--b) for the data bandpass filtered between 15 and 30 Hz.  In (a--d), the ACFs are sorted by increasing dynamic peak strain values, which are computed after bandpass filtering the strain waveforms in their respective frequency bands. (e--f) Dynamic peak strains after bandpass filtering the earthquake waveforms between 10-20 Hz and 15-30 Hz at channels 5000 and 7000, respectively.
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure3.png" width=75%/>
</p>
<br/>
<br/>
