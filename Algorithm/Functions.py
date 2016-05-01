from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
from skimage.morphology import dilation, watershed
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.segmentation import find_boundaries
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'

fig_size = 5

fig = disk


def local_otsu(image):
    radius = 150
    s_elem = disk(radius)
    local = rank.otsu(image, s_elem)
    return local


def global_otsu(image):
    threshold_global_otsu = threshold_otsu(image)
    _global = image >= threshold_global_otsu
    return _global


def watershed_separation(image, s_elem):
    distance = ndi.distance_transform_edt(image)
    local_maxi = peak_local_max(distance, indices=False, footprint=s_elem, labels=image)
    markers = ndi.label(local_maxi)[0]

    seg = watershed(-distance, markers, mask=image)

    lines = find_boundaries(seg, mode='outer', background=True)
    lines = dilation(lines, s_elem)
    lines2 = ndi.binary_fill_holes(lines)
    lines2 = lines2 - lines
    return lines2
