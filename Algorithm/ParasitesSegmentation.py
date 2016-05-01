from Algorithm import Functions
from skimage.morphology import disk, erosion, dilation
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


def parasites(image, cells):
    img = Functions.global_otsu(image)
    s_elem = Functions.fig(Functions.fig_size)
    cells = dilation(cells, s_elem)
    img = img - cells

    return img
