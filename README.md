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

* The **Figure_2.py** code plots the stacked CCFs computed after applying 1-bit normalisation to the continuous data recorded by all channels between virtual source 4000 and channel 4400 (Figure 2a). All the waveforms are bandpass filtered between 0.25 and 5 Hz.  A dispersion image is obtained from the causal part of the CCFs with a slant-stack algorithm  and is shown in Figure 2b. The black dots show the selected phase velocity dispersion points used to perform the inversion.
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure_2.png" width=75%/>
</p>
<br/>
<br/>

* The **Figure_3.py** code shows the stacked CCFs computed  with (Figure 3a) and  without (Figure 3b) applying 1-bit normalisation to the continuous data recorded by all channels between virtual source 4000 and channel 4400. All the waveforms are bandpass filtered between 0.25 and 5 Hz. (Figure 3c illustrates the dispersion image obtained from the CCFs shown in Figure 3a together with the selected phase dispersion points (black dots). Figure 3d  is the same as Figure 3c for the CCFs shown in Figure 2b. The white lines depicts the first 10 spatial aliasing lines (i.e., Equation 2 of the paper).
<figure>
 <img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure_3.png" width=75%/>
<figcaption align = "center"><b>Fig. 3</b></figcaption>
</figure>

<br/>
<br/>

* The **Figure_5.py** code shows 
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure_5.png" width=75%/>
</p>
<br/>
<br/>

* The **Figure_6.py** code shows d 
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure_6.png" width=75%/>
</p>
<br/>
<br/>
