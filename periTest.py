import matplotlib
matplotlib.rcParams["backend"]="TkAgg"
from peri import util
from peri.viz.interaction import OrthoViewer
im = util.RawImage('../../Downloads/small_confocal_image.tif')
OrthoViewer(im.get_image())

print(matplotlib.get_backend())
import Tkinter
from Tkinter import *
Tk().mainloop()
