# Python codes for `Understanding surface-wave modal content for high-resolution imaging of submarine sediments with Distributed Acoustic Sensing'

The codes are for the following manuscript:
- Viens, L., M. Perton, Z. Spica, K. Nishida, M. Shinohara, and T. Yamada (2022), Understanding surface-wave modal content for high-resolution imaging of submarine sediments with Distributed Acoustic Sensing, Geophys. J. Int., [doi:10.1093/gji/ggac420](https://academic.oup.com/gji/advance-article/doi/10.1093/gji/ggac420/6775077?utm_source=authortollfreelink&utm_campaign=gji&utm_medium=email&guestAccessKey=7fbc7d25-9c01-45b6-8c60-8deca59c72cd)  

## Description:
* The **Codes** folder contains the six Python codes to reproduce the main figures of the paper (i.e., Figures 2, 3, 5, 6 ,7, and 10). Please contact Loïc Viens (lviens@lanl.gov) if you are interested in the codes and data to reproduce the other figures of the manuscript.

* The **Data** folder contains the data to reproduce the figures.
  

* The **Figures** folder contains 6 figures that can be plotted with the codes. 


## Codes and their outputs:

* The **Figure_2.py** code plots the stacked CCFs computed after applying 1-bit normalisation to the continuous data recorded by all channels between virtual source 4000 and channel 4400 (Figure 2a). All the waveforms are bandpass filtered between 0.25 and 5 Hz.  A dispersion image is obtained from the causal part of the CCFs with a slant-stack algorithm  and is shown in Figure 2b. The black dots show the selected phase velocity dispersion points used to perform the inversion.


<p align = "center"> <b>Figure 2</b> </p>
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure_2.png" width=75%/>
</p>
<br/>
  <HR align=center size=8 width="100%" color="grey" >

* The **Figure_3.py** code shows the stacked CCFs computed  with (Figure 3a) and  without (Figure 3b) applying 1-bit normalisation to the continuous data recorded by all channels between virtual source 4000 and channel 4400. All the waveforms are bandpass filtered between 0.25 and 5 Hz. (Figure 3c illustrates the dispersion image obtained from the CCFs shown in Figure 3a together with the selected phase dispersion points (black dots). Figure 3d  is the same as Figure 3c for the CCFs shown in Figure 2b. The white lines depicts the first 10 spatial aliasing lines (i.e., Equation 2 of the paper).
<p align = "center"> <b>Figure 3</b> </p>

<p align="center">
  <img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure_3.png" width=75%/>
</p>
<br/>
  <HR align=center size=8 width="100%" color="grey" >

* The **Figure_5.py** code shows the dispersion images computed from 1-bit CCFs and by considering 400 receivers along the cable; every 500 virtual sources. Selected dispersion points, after rejecting spatial aliasing artefacts, are shown by the black dots.
<p align = "center"> <b>Figure 5</b> </p>
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure_5.png" width=75%/>
</p>
<br/>
  <HR align=center size=8 width="100%" color="grey" >

* The **Figure_6.py** code shows the simulations that we performed in step gradient media. Figure 6a displays the velocity models for two constant $V_S$ step gradients ($\Delta V_S/\Delta z={1,\ 2} \ s^{-1}$). (b) Theoretical DCs for the two velocity models shown in (a) using same colour code. (c) Theoretical dispersion image calculated from  horizontal strain waveforms excited by an horizontal force and using the velocity model with a gradient of $\Delta V_S/\Delta z=1\ s^{-1}$. The amplitude of the energy is normalised between 0 and 1 and the DCs from (b) are shown by the  black lines.
<p align = "center"> <b>Figure 6</b> </p>
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure_6.png" width=75%/>
</p>
<br/>
  <HR align=center size=8 width="100%" color="grey" >

* The **Figure_7.py** code shows examples of the inverted velocity models. Figure 7a shows the selected dispersion points (grey dots) and inverted DCs (black lines) for four sections along the cable. The virtual source number is indicated on top of each subplot. (b) Inverted $V_S$ velocity model (black) for the four sections shown in (a). $V_S$ gradient values and lines computed by fitting the inverted 1D $V_S$ models between the ocean floor and 400 m depth with a straight line are shown in blue.  
<p align = "center"> <b>Figure 7</b> </p>
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure_7.png" width=75%/>
</p>
<br/>
  <HR align=center size=8 width="100%" color="grey" >

* The **Figure_10.py** code displays the velocity model (Figure 10b) together with the strain waveforms of a Mw 3.7 earthquake bandpass filtered between 1.5 and 5 Hz  (Figure 10a). Note that the frequency content is slightly different from that in the paper (i.e., 2-8 Hz) as data were downsampled to 10 Hz to be uploaded on Github. Direct P- and S-waves arrive around 15 s and 25 s after the origin time, respectively. Regions where surface waves (SW) are locally generated are shown by the vertical red arrows.  Figure 10b shows a zoom on the shallow part of the inverted velocity model. The red arrows correspond to the regions where surface waves are generated.
<p align = "center"> <b>Figure 10</b> </p>
<p align="center">
<img src="https://github.com/lviens/2022_DAS_Tomography/blob/main/Figures/Figure_10.png" width=75%/>
</p>
<br/>
  <HR align=center size=8 width="100%" color="grey" >
