from Algorithm import Functions
from skimage.morphology import erosion, dilation
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

    return Functions.watershed_separation(img, s_elem)

