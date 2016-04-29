from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


def local_otsu(image):
    radius = 150
    selem = disk(radius)
    local = rank.otsu(image, selem)
    return local


def global_otsu(image):
    threshold_global_otsu = threshold_otsu(image)
    _global = image >= threshold_global_otsu
    return _global