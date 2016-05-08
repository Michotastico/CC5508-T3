from Algorithm import Functions
import numpy as np
from skimage.morphology import binary_dilation, watershed
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.segmentation import find_boundaries
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


def raster(cells):
    s_elem = Functions.fig(Functions.fig_size)
    image = cells.copy()

    image = np.invert(image)

    distance = ndi.distance_transform_edt(image)
    local_maxi = peak_local_max(distance, indices=False, footprint=s_elem, labels=image)
    markers = ndi.label(local_maxi)[0]
    seg2 = watershed(distance, markers)

    lines = find_boundaries(seg2, mode='outer', background=True)
    lines = binary_dilation(lines, s_elem)

    return lines

