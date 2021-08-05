## SOUP-GAN: 

Super-resolution interpolation tool for medical images.

This inference code supports: 

1) Thick-slices to thin-slices SR interpolation with arbitrarily user-selected sampling ratios. 
2) Medical imaging mask inerpolation.

#
[SOUP-GAN: Super-Resolution MRI Using Generative Adversarial Networks](https://arxiv.org/abs/2106.02599)

[Kuan Zhang](https://www.mayo.edu/research/labs/radiology-informatics/faculty-staff), Haoji Hu, [Kenneth Philbrick](https://www.linkedin.com/in/kenneth-philbrick-1b164bb), [Gian Marco Conte](https://www.mayo.edu/research/labs/radiology-informatics/faculty-staff), [Joseph D. Sobek](https://www.mayo.edu/research/labs/radiology-informatics/faculty-staff), [Pouria Rouzrokh](https://www.mayo.edu/research/labs/radiology-informatics/faculty-staff), [Bradley J. Erickson](https://www.mayo.edu/research/faculty/erickson-bradley-j-m-d-ph-d/bio-00077505)
#
#### Usage:

Install the package [KevinSR](https://pypi.org/project/KevinSR/). 

from KevinSR import mask_interpolation, SOUP_GAN

\# for SR image interp 

thin_slices = SOUP_GAN(thick_slices, factor)

\# for mask interp 

new_masks = mask_interpolation(masks, factor)


#### Example:
<img src="Example_1.png" width="600" height="600" align="middle"/>

<img src="mask_interp.png" width="600" align="middle"/>
