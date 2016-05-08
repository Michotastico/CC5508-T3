from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
from skimage.morphology import binary_dilation, watershed
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.segmentation import find_boundaries
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'

fig_size = 5
fig = disk
iterations = 3


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
    lines = binary_dilation(lines, s_elem)
    return subtraction(image, lines)


def subtraction(img1, img2):
    size = img1.shape
    return_image = img1.copy()
    for x in range(size[0]):
        for y in range(size[1]):
            if img1[x,y] == 0:
                return_image[x,y] = 0
            else:
                value = img1[x,y] - img2[x,y]
                if value < 0:
                    value = 0
                return_image[x,y] = value
    return return_image
