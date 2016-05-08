from skimage import io
import matplotlib.pyplot as plt
from Algorithm import BeWo, ParasitesSegmentation, Voronoi
import numpy as np
import Algorithm.Functions as Functions
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'

image = io.imread('Images/imagen5.tiff')
size = image.shape

color_image = np.empty((size[0], size[1], 3))

cells = BeWo.cells(image)

centers_of_mass = Functions.center_of_mass(cells)
print "Cells: " + str(len(centers_of_mass))

voronoi = Voronoi.raster(cells)

centers_of_mass_voronoi = Functions.center_of_mass_max_area(-voronoi)

parasites = ParasitesSegmentation.parasites(image, cells, voronoi)

print "Parasites: " + str(len(Functions.center_of_mass(parasites)))


color_image[:,:,0] = cells
color_image[:,:,1] = parasites
color_image[:,:,2] = voronoi

color_original = Functions.add_cm(color_image, centers_of_mass, 1)
color_original = Functions.add_cm(color_original, centers_of_mass_voronoi, 2)

fig, ((img, bewo, paras), (voro, masa, rgb)) = plt.subplots(nrows=2, ncols=3, figsize=(10, 5))

img.imshow(image, cmap=plt.cm.gray)
bewo.imshow(cells, cmap=plt.cm.gray)
paras.imshow(parasites, cmap=plt.cm.gray)
voro.imshow(voronoi, cmap=plt.cm.gray)
masa.imshow(color_original)
rgb.imshow(color_image)

fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0.02, left=0.02, right=0.98)

plt.show()