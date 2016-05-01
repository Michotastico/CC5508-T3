from Algorithm import Functions
from skimage.morphology import erosion, dilation, watershed
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.segmentation import find_boundaries, clear_border
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

    distance = ndi.distance_transform_edt(img)
    local_maxi = peak_local_max(distance, indices=False, footprint=s_elem, labels=img)
    markers = ndi.label(local_maxi)[0]

    seg = watershed(-distance, markers, mask=img)
    lines = find_boundaries(seg, mode='outer', background=True)
    lines = dilation(lines, s_elem)
    lines2 = ndi.binary_fill_holes(lines)
    lines2 = lines2-lines

    return lines2

