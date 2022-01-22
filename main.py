# CS194-26 (CS294-26): Project 1 starter Python code

# these are just some suggested libraries
# instead of scikit-image you could use matplotlib and opencv to read, write, and display images

import numpy as np
import skimage as sk
import skimage.io as skio

from matplotlib import pyplot as plt

# find the best allignment of two channels, Single Scale
def align_ss(u, v):
    # start with max value
    lowScore = 999999999
    for x in range(-15, 16):
        for y in range(-15, 16):
            temp = np.roll(u, x, axis=0)
            temp = np.roll(temp, y, axis=1)
            score = np.sum( (temp-v)**2)
            if(score < lowScore):
                lowScore = score
                bestX = x
                bestY = y
    print('Best x: '+ str(bestX))
    print('Best Y: '+ str(bestY))
    temp = np.roll(u, bestX, axis=0)
    temp = np.roll(temp, bestY, axis=1)
    return temp

# name of the input file
imname = './data/31421v.jpg'

# read in the image
im = skio.imread(imname)

# convert to double (might want to do this later on to save memory)    
im = sk.img_as_float(im)
    
# compute the height of each part (just 1/3 of total)
height = int(np.floor(im.shape[0] / 3.0))

# separate color channels
b = im[:height]
g = im[height: 2*height]
r = im[2*height: 3*height]

# align the images
# functions that might be useful for aligning the images include:
# np.roll, np.sum, sk.transform.rescale (for multiscale)

ag = align_ss(g, b)
ar = align_ss(r, b)

# create a color image
im_out = np.dstack([ar, ag, b])
im_base = np.dstack([r,g,b])

# save the image
fname = '/out_path/out_fname.jpg'
#skio.imsave(fname, im_out)

# display the image
skio.imshow(im_base)
plt.show()
skio.imshow(im_out)
plt.show()