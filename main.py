# CS194-26 (CS294-26): Project 1 starter Python code

# these are just some suggested libraries
# instead of scikit-image you could use matplotlib and opencv to read, write, and display images

import numpy as np
import skimage as sk
import skimage.io as skio

from skimage.transform import rescale
from matplotlib import pyplot as plt

def align_ms(u, v):
    tempU = rescale(u, .25)
    tempV = rescale(v, .25)

    al, x1, y1 = align_ss(tempU,tempV, 20)
    print("25%")

    tempU = rescale(u, .5)
    tempV = rescale(v, .5)
    tempU = np.roll(tempU, (x1*2), axis=0)
    tempU = np.roll(tempU, (y1*2), axis=1)

    al, x2, y2 = align_ss(tempU,tempV, 10)
    print("50%")

    tempU = u
    tempV = v
    tempU = np.roll(tempU, ((x2*2)+(x1*4)), axis=0)
    tempU = np.roll(tempU, ((y2*2)+(y1*4)), axis=1)

    al, x, y = align_ss(tempU,tempV, 5)
    print("100%")

    return al

# find the best allignment of two channels, Single Scale, rng is the range of pixels the channels will slide in both directions
# range should be positive
def align_ss(u, v, rng):
    # start with max value
    lowScore = 999999999

    #check a 30 pixel range in x and y direction
    for x in range(-1*(rng), (rng+1)):
        for y in range(-1*(rng), (rng+1)):
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
    return temp, bestX, bestY

# name of the input file
#imname = './data/01047u.jpg'
imname = input("Enter image path: ")

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

# single scale
#ag, x, y = align_ss(g, b, 15)
#ar, x, y = align_ss(r, b, 15)

# multi scale
ag = align_ms(g, b)
ar = align_ms(r, b)

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