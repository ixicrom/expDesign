import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

import pims
import trackpy as tp

from skimage import io

# image=pims.TiffStack('/Volumes/PhD/expDesign/2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_NBD_xyz007_x100_z35_K4.tif')
im = io.imread('/Volumes/PhD/expDesign/2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_NBD_xyz007_x100_z35_K4.tif', as_gray=True)
im_array = np.array(im)
im.shape
im_array_small = im_array[:,312:, 0:200]
im_array_small.shape
f=tp.locate(im_array,diameter=(3,11,11))
f_small = tp.locate(im_array_small,diameter=(3,11,11))

# plt.figure()
# tp.annotate3d(f[f['z']==f['z']],im_array)
plt.imshow(im_array_small[2,:,:],cmap="gray")
scatter = plt.scatter(x=f_small["x"],y=f_small["y"], c=f_small["z"],marker="x")
plt.legend(*scatter.legend_elements(), title="z")
plt.show()
