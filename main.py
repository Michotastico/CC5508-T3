from skimage import io
import matplotlib.pyplot as plt
from Algorithm import Functions, BeWo
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


image = io.imread('Images/imagen5.tiff')

#g_otsu = Functions.global_otsu(image)
proccessed = BeWo.cells(image)

fig, (img, other) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

img.imshow(image,cmap=plt.cm.gray)
other.imshow(proccessed,cmap=plt.cm.gray)

fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0.02, left=0.02, right=0.98)

plt.show()