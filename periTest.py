import matplotlib
matplotlib.rcParams["backend"]="TkAgg" #with OrthoViewer this gives an error that 'this isn't a Tk application'
from peri import util
from peri.viz.interaction import OrthoViewer
im = util.RawImage('../../Downloads/small_confocal_image.tif')
OrthoViewer(im.get_image())

matplotlib.pyplot.show(block = True)


# print(matplotlib.get_backend())
# import Tkinter
# from Tkinter import *
# Tk().mainloop()
