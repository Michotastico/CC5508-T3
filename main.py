from Algorithm import AutomatedCellCounter
__author__ = 'Michel Llorens A.'
__email__ = 'mllorens@dcc.uchile.cl'

images = ['imagen0.tiff', 'imagen1.tiff', 'imagen2.tiff', 'imagen3.tiff', 'imagen4.tiff', 'imagen5.tiff',
          'imagen6.tiff', 'imagen7.tiff', 'imagen8.tiff', 'imagen9.tiff']
for image in images:
    counter = AutomatedCellCounter.Acc(image)
    counter.save()