import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

import pims
import trackpy as tp

from skimage import io

image=pims.TiffStack('../2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_NBD_xyz007_x100_z35_K4.tif')
im = io.imread('../2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_NBD_xyz007_x100_z35_K4.tif', as_gray=True)
im_array = np.array(im)

f=tp.locate(im_array,diameter=(3,11,11))

plt.figure()
tp.annotate3d(f[f['z']==f['z']],im_array)
