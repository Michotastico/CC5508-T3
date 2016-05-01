from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'

fig_size = 10

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
