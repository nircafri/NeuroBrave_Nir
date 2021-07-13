import scipy.io
import numpy as numpy
from PIL import Image
import imageio
import matplotlib.pyplot as plt
import array as arr

FeatureMat_timeWin = scipy.io.loadmat('FeatureMat_timeWin.mat')
images = scipy.io.loadmat('images.mat')
trials_subNums = scipy.io.loadmat('trials_subNums.mat')

subjNum = trials_subNums['subjectNum'][0]
img = images['img']
features = FeatureMat_timeWin['features']
Label = (features[:, -1] - 1).astype(int)

red = img[:, 0, :, :]
Green = img[:, 1, :, :]
Blue = img[:, 2, :, :]
for pic in range(0,10):
    data = numpy.array([red[pic, :, :], Green[pic, :, :], Blue[pic, :, :]])
    dataSwap = numpy.swapaxes(data,0,2)
    img = Image.fromarray(dataSwap, 'RGB')
    img.save(str(pic)+"your_file.jpeg")

    img.show()
# subjIndexes = {}
# for t in range(0,numpy.max(subjNum)):
#     subjIndexes{t} = numpy.where(subjNum == t)
