from Algorithm import Functions
from skimage.morphology import disk, erosion, dilation , watershed
# import numpy as np
from scipy import ndimage as ndi
# from skimage.feature import peak_local_max
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'

iterations = 3


def cells(image):
    img = Functions.global_otsu(image)
    s_elem = Functions.fig(Functions.fig_size)
    for i in range(iterations):
        img = erosion(img, s_elem)
    for i in range(iterations):
        img = dilation(img, s_elem)

    # distance = ndi.distance_transform_edt(img)
    # img = watershed(img, -distance, s_elem)
    # distance = ndi.distance_transform_edt(img)
    # local_maxi = peak_local_max(distance, indices=False, footprint=np.ones((3, 3)), labels=img)
    # markers = ndi.label(local_maxi)[0]

    # segmentation = watershed(-distance, markers, mask=img)
    return img # segmentation

