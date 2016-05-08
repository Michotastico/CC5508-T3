from skimage import io
import matplotlib.pyplot as plt
from Algorithm import BeWo, ParasitesSegmentation, Voronoi
import numpy as np
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


image = io.imread('Images/imagen5.tiff')

cells = BeWo.cells(image)

voronoi = Voronoi.raster(cells)

parasites = ParasitesSegmentation.parasites(image, cells, voronoi)

size = image.shape

color_image = np.full((size[0], size[1], 3), 0)
color_image[:,:,0] = cells
color_image[:,:,1] = parasites
color_image[:,:,2] = voronoi


fig, ((img, bewo, paras), (voro, masa, rgb)) = plt.subplots(nrows=2, ncols=3, figsize=(10, 5))

img.imshow(image, cmap=plt.cm.gray)
bewo.imshow(cells, cmap=plt.cm.gray)
paras.imshow(parasites, cmap=plt.cm.gray)
voro.imshow(voronoi, cmap=plt.cm.gray)
masa.imshow(voronoi, cmap=plt.cm.gray)
rgb.imshow(color_image)

fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0.02, left=0.02, right=0.98)

plt.show()