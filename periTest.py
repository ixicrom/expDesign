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

from datetime import datetime

im = util.RawImage('/Volumes/PhD/expDesign/Data/2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_NBD_xyz007_x100_z35_K4.tif')

tile = util.Tile([5,312,0],right=[12,512,200])
small_im = util.RawImage('/Volumes/PhD/expDesign/Data/2011_DAS_SoftMatter_Data/jtLLF090701_BR090729_NBD_xyz007_x100_z35_K4.tif', tile=tile)
zpixel=0.82
xpixel=35.2/512
zscale=zpixel/xpixel

particle_positions = np.load('part_loc_smallSlice.npy')
particle_radii = 8.0
particles = objs.PlatonicSpheresCollection(particle_positions, particle_radii, zscale=zscale)
# imaginary_slide = objs.Slab(zpos=6)
print(particles)
objects = comp.comp.ComponentCollection([particles], category='obj')

# OrthoPrefeature(im.get_image(), particle_positions, viewrad=3.0)



background = comp.ilms.LegendrePoly2P1D(order=(4,2,2), category='bkg')
illumination = comp.ilms.BarnesStreakLegPoly2P1D(npts=(4, 2, 2))
offset = comp.GlobalScalar(name='offset', value=0.)
point_spread_function = comp.exactpsf.FixedSSChebLinePSF(pxsize=xpixel)
model = models.ConfocalDyedParticlesModel()
st = states.ImageState(small_im, [objects, illumination, background, point_spread_function], mdl=model)
st.update('zscale', zscale)
savefile = "/Volumes/PhD/expDesign/states/"+datetime.now().strftime("%Y%m%d-%H%M%S") + "_unoptimized"
states.save(st,savefile)
# st.update('psf-laser-wavelength', .488)
runner.link_zscale(st)

runner.optimize_from_initial(st)
savefile = "/Volumes/PhD/expDesign/states/"+datetime.now().strftime("%Y%m%d-%H%M%S") + "_inital_optimized"
states.save(st,savefile)
runner.finish_state(st)
