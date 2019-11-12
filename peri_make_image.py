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


imFile = '/Volumes/PhD/expDesign/test/balls.tif'
blank_im = util.RawImage(imFile)
particle_positions=np.load('part_loc_davidImage.npy')
# particle_positions
n=100
# random_particles = np.c_[np.random.random(n), np.random.random(n),np.zeros(n)]*200.0
tile = util.Tile(200)
small_im = util.RawImage(imFile, tile=tile)

zpixel=1
xpixel=1
zscale=zpixel/xpixel

particle_radii = 8.0
particles = objs.PlatonicSpheresCollection(particle_positions, particle_radii, zscale=zscale)

objects = comp.comp.ComponentCollection([particles], category='obj')


background = comp.ilms.LegendrePoly2P1D(order=(4,2,2), category='bkg')
illumination = comp.ilms.BarnesStreakLegPoly2P1D(npts=(4, 2, 2))
offset = comp.GlobalScalar(name='offset', value=0.)
point_spread_function = comp.exactpsf.ChebyshevLineScanConfocalPSF(pxsize=xpixel)
model = models.ConfocalDyedParticlesModel()
st = states.ImageState(small_im, [objects, illumination, background, point_spread_function], mdl=model)
st.update('zscale', zscale)
savefile = "/Volumes/PhD/expDesign/test/"+datetime.now().strftime("%Y%m%d-%H%M%S") + "_unoptimized"
runner.link_zscale(st)
runner.optimize_from_initial(st)
savefile = "/Volumes/PhD/expDesign/test/"+datetime.now().strftime("%Y%m%d-%H%M%S") + "_inital_optimized"
states.save(st,savefile)

# new_st = runner.get_particles_featuring(8)
