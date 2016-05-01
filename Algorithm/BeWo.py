from Algorithm import Functions
from skimage.morphology import binary_erosion, binary_dilation
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


def cells(image):
    img = Functions.global_otsu(image)
    s_elem = Functions.fig(Functions.fig_size)
    for i in range(Functions.iterations):
        img = binary_erosion(img, s_elem)
    for i in range(Functions.iterations):
        img = binary_dilation(img, s_elem)

    return Functions.watershed_separation(img, s_elem)

