from skimage import io
import matplotlib.pyplot as plt
from Algorithm import BeWo, ParasitesSegmentation
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


image = io.imread('Images/imagen1.tiff')

cells = BeWo.cells(image)

parasites = ParasitesSegmentation.parasites(image, cells)

fig, (img, bewo, paras) = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))

img.imshow(image, cmap=plt.cm.gray)
bewo.imshow(cells, cmap=plt.cm.gray)
paras.imshow(parasites, cmap=plt.cm.gray)

fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0.02, left=0.02, right=0.98)

plt.show()