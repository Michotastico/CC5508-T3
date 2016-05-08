from Algorithm import Functions
from skimage.morphology import binary_erosion, binary_dilation, binary_opening
import matplotlib.pyplot as plt
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


def parasites(image, cells):
    img = Functions.global_otsu(image)
    cells = Functions.global_otsu(cells)
    s_elem = Functions.fig(Functions.fig_size)
    cells = binary_dilation(cells, s_elem)
    return_image = Functions.subtraction(img, cells)
    for i in range(Functions.iterations-1):
        return_image = binary_erosion(return_image)
    return_image = binary_opening(return_image)
    for i in range(Functions.iterations - 1):
        return_image = binary_dilation(return_image)
    return return_image
