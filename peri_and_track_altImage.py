from peri import util
import numpy as np
from peri.comp import objs
from peri.viz.interaction import OrthoPrefeature
from peri import models
from peri import states
from peri import comp
from peri import runner
from peri.viz import plots
import matplotlib as mpl

import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series
import pims
import trackpy as tp
# from skimage import io
from datetime import datetime

imFile = '/Volumes/PhD/expDesign/Data/David/6-5a.tif'
# im = io.imread(imFile)
# im_array = np.array(im)
# print(im_array.shape)
# im_array_small = im_array[5:,312:, 0:200]
# im_array_small
# f=tp.locate(im_array,diameter=(9,9,9))
# f[f['z']==f['z']]
# f_small = tp.locate(im_array_small,diameter=(9,9,9))
# f_small=f_small[f_small['z']==f_small['z']]
# np.save('part_loc_davidImage.npy', np.array(f[f.columns[0:3,]]))
# particle_positions = np.array(f_small[f_small.columns[0:3,]])

raw_im = util.RawImage(imFile)
im_arr = raw_im.get_image()
f=tp.locate(im_arr,diameter=(9,9,9))

tile = util.Tile(200)
small_im = util.RawImage(imFile, tile=tile)
small_im_arr = small_im.get_image()
f_small = tp.locate(small_im_arr, diameter=(9,9,9))
particle_positions = np.array(f_small[f_small.columns[0:3,]])

zpixel=1
xpixel=1
zscale=zpixel/xpixel

particle_radii = 8.0
particles = objs.PlatonicSpheresCollection(particle_positions, particle_radii, zscale=zscale)

objects = comp.comp.ComponentCollection([particles], category='obj')

# OrthoPrefeature(im.get_image(), particle_positions, viewrad=3.0)



background = comp.ilms.LegendrePoly2P1D(order=(4,2,2), category='bkg')
illumination = comp.ilms.BarnesStreakLegPoly2P1D(npts=(4, 2, 2))
offset = comp.GlobalScalar(name='offset', value=0.)
point_spread_function = comp.exactpsf.ChebyshevLineScanConfocalPSF(pxsize=xpixel)
model = models.ConfocalDyedParticlesModel()
st = states.ImageState(small_im, [objects, illumination, background, point_spread_function], mdl=model)
st.update('zscale', zscale)
savefile = "/Volumes/PhD/expDesign/states/David"+datetime.now().strftime("%Y%m%d-%H%M%S") + "_unoptimized"
states.save(st,savefile)
# st.update('psf-laser-wavelength', .488)
runner.link_zscale(st)

runner.optimize_from_initial(st)
savefile = "/Volumes/PhD/expDesign/states/"+datetime.now().strftime("%Y%m%d-%H%M%S") + "_inital_optimized"
states.save(st,savefile)
runner.finish_state(st)
