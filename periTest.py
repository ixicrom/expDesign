import matplotlib
# matplotlib.rcParams["backend"]="TkAgg"
from peri import util
import numpy as np
from peri.comp import objs
from peri.viz.interaction import OrthoPrefeature
from peri import models
from peri import states
from peri import comp

im = util.RawImage('/Volumes/PhD/expDesign/2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_NBD_xyz007_x100_z35_K4.tif')

tile = util.Tile([0,312,0],right=[12,512,200])
small_im = util.RawImage('/Volumes/PhD/expDesign/2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_NBD_xyz007_x100_z35_K4.tif', tile=tile)

particle_positions = np.load('/Volumes/PhD/expDesign/Python/particles1.npy')
particle_radii = 8.0
particles = objs.PlatonicSpheresCollection(particle_positions, particle_radii)
# imaginary_slide = objs.Slab(zpos=6)

# objects = comp.comp.ComponentCollection([particles], category='obj')

illumination = comp.ilms.LegendrePoly2P1D()

background = comp.ilms.LegendrePoly2P1D(category='bkg')

point_spread_function = comp.psfs.AnisotropicGaussian

offset = comp.comp.GlobalScalar(name='offset', value=0.)

# OrthoPrefeature(im.get_image(), particle_positions, viewrad=3.0)

model = models.ConfocalImageModel()

st = states.ImageState(im, [particles, illumination, background, point_spread_function, offset], mdl=model)
