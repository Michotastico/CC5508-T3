from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
from skimage.morphology import binary_dilation, watershed
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage.segmentation import find_boundaries
import matplotlib.pyplot as plt
from skimage.draw import circle
from skimage.measure import regionprops
from skimage.measure import label as Label
import numpy as np
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'

fig_size = 5
fig = disk
iterations = 3


def local_otsu(image):
    radius = 12
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


def center_of_mass(image):
    label, n = ndi.label(image)
    indexes = range(1, n+1)
    centers = ndi.measurements.center_of_mass(image, label, indexes)
    return centers


def center_of_mass_max_area(image):
    label, n = ndi.label(image)
    props = regionprops(Label(image))
    index = 0
    area = 0
    for i in range(len(props)):
        if props[i].area > area:
            area = props[i].area
            index = i
    indexes = [0] * n
    indexes[index] = 1
    centers = ndi.measurements.center_of_mass(image, label, indexes)
    return centers


def center_with_parasites(voronoi, cm_parasites):
    image = -voronoi
    props = regionprops(Label(image))
    big_counter = 0
    for i in range(len(props)):
        counter = 0
        for parasite in cm_parasites:
            if parasite in props[i].coords:
                counter += 1
        if counter > 3:
            big_counter += 1
    return big_counter


def add_cm(image, centers, color):
    return_image = image.copy()
    for center in centers:
        rr, cc = circle(center[0], center[1], 10)
        return_image[rr, cc, 0] = 1
        return_image[rr, cc, color] = 1
    return return_image


def plot_comparison(original, filtered, filter_name):

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4), sharex=True,
                                   sharey=True)
    ax1.imshow(original)
    ax1.set_title('original')
    ax1.axis('off')
    ax1.set_adjustable('box-forced')
    ax2.imshow(filtered)
    ax2.set_title(filter_name)
    ax2.axis('off')
    ax2.set_adjustable('box-forced')

    plt.show()
