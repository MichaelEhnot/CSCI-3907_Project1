from skimage import data, io
from matplotlib import pyplot as plt

# name of the input file
imname = './data/00056v.jpg'

# read in the image
im = io.imread(imname)

io.imshow(im)
plt.show()