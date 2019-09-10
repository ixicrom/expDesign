import matplotlib
# matplotlib.rcParams["backend"]="TkAgg"
from peri import util
import numpy as np
from peri.comp import objs
from peri.viz.interaction import OrthoPrefeature
from peri import models
from peri import states
from peri import comp
from peri import runner
from peri.viz import plots


im = util.RawImage('/Volumes/PhD/expDesign/2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_RhB_xyz007_x100_z35_K4.tif')

tile = util.Tile([5,312,0],right=[12,512,200])
tile
small_im = util.RawImage('/Volumes/PhD/expDesign/2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_RhB_xyz007_x100_z35_K4.tif', tile=tile)

particle_positions = np.load('part_loc_smallSlice.npy')
particle_radii = 8.0
particles = objs.PlatonicSpheresCollection(particle_positions, particle_radii)
# imaginary_slide = objs.Slab(zpos=6)

objects = comp.comp.ComponentCollection([particles], category='obj')

# illumination = comp.ilms.Polynomial3D(order=(1,1,1))
# # illumination = comp.ilms.BarnesStreakLegPoly2P1D(npts=(16, 10, 8, 4), zorder=8)
#
# # background = comp.ilms.LegendrePoly2P1D(category='bkg')
# background = comp.ilms.LegendrePoly2P1D(order=(7,2,2), category='bkg')
#
# # point_spread_function = comp.psfs.AnisotropicGaussian
# point_spread_function = comp.exactpsf.FixedSSChebLinePSF()
#
# offset = comp.comp.GlobalScalar(name='offset', value=0.)
# # offset = comp.GlobalScalar(name='offset', value=0.)
#
# # OrthoPrefeature(im.get_image(), particle_positions, viewrad=3.0)
#
# model = models.ConfocalImageModel()
#
# st = states.ImageState(small_im, [particles, illumination, background, point_spread_function, offset], mdl=model)
#
# runner.link_zscale(st)
# print(st.error)
#
# runner.optimize_from_initial(st)
#
#
# tile2 = util.Tile([11,312,0],right=[12,512,200])
# tile2
# plots.compare_data_model_residuals(st, tile=tile2)
#
# plots.examine_unexplained_noise(st)
zpixel=0.82
xpixel=35.2/512
zpixel/xpixel

background = comp.ilms.LegendrePoly2P1D(order=(3,2,2), category='bkg')
illumination = comp.ilms.BarnesStreakLegPoly2P1D(npts=(4, 2, 2))
offset = comp.GlobalScalar(name='offset', value=0.)
point_spread_function = comp.exactpsf.FixedSSChebLinePSF(pxsize=xpixel)
model = models.ConfocalDyedParticlesModel()
st = states.ImageState(small_im, [objects, illumination, background, point_spread_function], mdl=model)
st.update('zscale', zpixel/xpixel)
# st.update('psf-laser-wavelength', .488)
runner.link_zscale(st)

runner.optimize_from_initial(st)
runner.finish_state(st)
