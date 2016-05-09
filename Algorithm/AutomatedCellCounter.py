from skimage import io
import matplotlib.pyplot as plt
from Algorithm import BeWo, ParasitesSegmentation, Voronoi
import numpy as np
import Algorithm.Functions as Functions
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'


class Acc:
    def __init__(self, image):
        self.path = image
        self.image = io.imread('Images/'+image)
        size = self.image.shape
        print_init = "Image: " + image + "\n"
        print print_init
        self.color_image = np.empty((size[0], size[1], 3))
        self.cells = BeWo.cells(self.image)

        centers_of_mass = Functions.center_of_mass(self.cells)

        self.voronoi = Voronoi.raster(self.cells)
        centers_of_mass_voronoi = Functions.center_of_mass_max_area(-self.voronoi)

        self.parasites = ParasitesSegmentation.parasites(self.image, self.cells, self.voronoi)
        parasites_center = Functions.center_of_mass(self.parasites)

        cells_with_parasites = str(Functions.center_with_parasites(self.voronoi, parasites_center))

        fo = open('Results/'+self.path+".txt", "w+")
        fo.write(print_init)
        fo.write("Cells: " + str(len(centers_of_mass)) + "\n")
        for center in centers_of_mass_voronoi:
            if str(center[0]) != "nan" or str(center[1]) != "nan":
                c = "(" + str(center[0]) + ", " + str(center[1]) + ")"
                fo.write("Biggest area:" + c + "\n")

        fo.write("Parasites: " +  str(len(parasites_center)) + "\n")
        fo.write("Cells with at least 3 parasites: " + cells_with_parasites)
        fo.close()

        print "Data stored"

        self.color_image[:, :, 0] = self.cells
        self.color_image[:, :, 1] = self.parasites
        self.color_image[:, :, 2] = self.voronoi

        self.color_original = Functions.add_cm(self.color_image, centers_of_mass, 1)
        self.color_original = Functions.add_cm(self.color_original, centers_of_mass_voronoi, 2)

    def save(self):
        fig, ((img, bewo, paras), (voro, masa, rgb)) = plt.subplots(nrows=2, ncols=3, figsize=(10, 5))

        img.imshow(self.image, cmap=plt.cm.gray)
        bewo.imshow(self.cells, cmap=plt.cm.gray)
        paras.imshow(self.parasites, cmap=plt.cm.gray)
        voro.imshow(self.voronoi, cmap=plt.cm.gray)
        masa.imshow(self.color_original)
        rgb.imshow(self.color_image)

        img.axis('off')
        bewo.axis('off')
        paras.axis('off')
        voro.axis('off')
        masa.axis('off')
        rgb.axis('off')

        fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0.02, left=0.02, right=0.98)

        plt.savefig('Results/'+self.path, bbox_inches='tight')

        print "Figure stored"