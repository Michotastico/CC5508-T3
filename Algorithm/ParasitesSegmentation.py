from Algorithm import Functions
from skimage.morphology import binary_erosion, binary_dilation, binary_opening
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


def parasites(image, cells, voronoi):
    img = Functions.global_otsu(image)
    cells = Functions.global_otsu(cells)
    s_elem = Functions.fig(Functions.fig_size)

    # Remove cells

    for i in range(Functions.iterations):
        cells = binary_dilation(cells, s_elem)
    return_image = Functions.subtraction(img, cells)

    # Remove stuff from cells

    for i in range(Functions.iterations-1):
        return_image = binary_erosion(return_image)
    return_image = binary_opening(return_image)
    for i in range(Functions.iterations - 1):
        return_image = binary_dilation(return_image)

    # Remove bigger objects

    removal_image = return_image.copy()

    for i in range(Functions.iterations + 5):
        removal_image = binary_erosion(removal_image)
    removal_image = binary_opening(removal_image)
    for i in range(Functions.iterations + 10):
        removal_image = binary_dilation(removal_image)

    return_image = Functions.subtraction(return_image, removal_image)

    # Remove voronoi lines for better quality
    return Functions.subtraction(return_image, voronoi)
