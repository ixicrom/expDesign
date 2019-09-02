from peri import util
from peri.viz.interaction import OrthoViewer
import matplotlib

im = util.RawImage('../../Downloads/small_confocal_image.tif')

import numpy
from peri.comp import objs
coverslip = objs.Slab(zpos=6)
particle_positions = numpy.load('../../Downloads/particle-positions.npy')
particle_radii = 5.0
particles = objs.PlatonicSpheresCollection(particle_positions, particle_radii)

from peri.comp import comp
objects = comp.ComponentCollection([particles, coverslip], category = 'obj')

from peri.comp import ilms
illumination = ilms.BarnesStreakLegPoly2P1D(npts=(16, 10, 8, 4), zorder=8)

background = ilms.LegendrePoly2P1D(order=(7,2,2), category='bkg')

offset = comp.GlobalScalar(name='offset', value=0.)

from peri.comp import exactpsf
point_spread_function = exactpsf.FixedSSChebLinePSF()

from peri import models
model = models.ConfocalImageModel()

print(model)

from peri import states
st = states.ImageState(im, [objects, illumination, background, point_spread_function, offset], mdl=model)
