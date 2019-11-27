import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# import pims
from peri.util import RawImage, Tile
import trackpy as tp

# from skimage import io

# image=pims.TiffStack('/Volumes/PhD/expDesign/2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_NBD_xyz007_x100_z35_K4.tif')
# im = io.imread('/Volumes/PhD/DavidData/Emily/2014_5_23-T3Y_63xoil_1.lsm', as_gray=True)
# im_array = np.array(im)
# im.shape
# im_array_small = im_array[5:,312:, 0:200]
# im_array_small.shape
# f=tp.locate(im_array,diameter=(3,11,11))
# f[f['z']==f['z']]
# f_small = tp.locate(im_array_small,diameter=(3,11,11))
# f_small=f_small[f_small['z']==f_small['z']]
# np.save('part_loc_T3Y_1.npy', np.array(f[f.columns[0:3,]]))

imFile = '/Volumes/PhD/DavidData/Emily/2014_5_23-T3Y_63xoil_1.lsm'
raw_im = RawImage(imFile)
im_arr = raw_im.get_image()
im_arr.shape()
f=tp.locate(im_arr,diameter=(9,9,9))

tile = Tile(200)
small_im = RawImage(imFile, tile=tile)
small_im_arr = small_im.get_image()
f_small = tp.locate(small_im_arr, diameter=(9,9,9))
particle_positions = np.array(f_small[f_small.columns[0:3,]])
np.save('part_loc_T3Y_1.npy', particle_positions)


# plt.figure()
# tp.annotate3d(f[f['z']==f['z']],im_array)
plt.imshow(im_array[2,:,:],cmap="gray")
scatter = plt.scatter(x=f["x"],y=f["y"], c=f["z"],marker="x")
plt.legend(*scatter.legend_elements(), title="z")
plt.show()
