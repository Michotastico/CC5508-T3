from Algorithm import Functions
from skimage.morphology import disk, erosion, dilation, watershed
import numpy as np
from skimage.filters import sobel
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'

iterations = 3


def cells(image):
    img = Functions.global_otsu(image)
    selem = disk(12)
    for i in range(iterations):
        img = erosion(img, selem)
    for i in range(iterations):
        img = dilation(img, selem)

    markers = np.zeros_like(img)
    markers[img < 30] = 1
    markers[img > 150] = 2
    elevation_map = sobel(img)
    segmentation = watershed(elevation_map, markers, mask=img)

    return segmentation