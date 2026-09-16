# CS180 (CS280A): Project 1 starter Python code

# these are just some suggested libraries
# instead of scikit-image you could use matplotlib and opencv to read, write, and display images

import numpy as np
import skimage as sk
import skimage.io as skio
from skimage.transform import rescale

# name of the input file
file_name = "emir"
imname = f'images/{file_name}.tif'

# read in the image
im = skio.imread(imname)

# convert to double (might want to do this later on to save memory)
im = sk.img_as_float(im)
    
# compute the height of each part (just 1/3 of total)
height = np.floor(im.shape[0] / 3.0).astype(int)

# separate color channels
b = im[:height]
g = im[height: 2*height]
r = im[2*height: 3*height]

# align the images
# functions that might be useful for aligning the images include:
# np.roll, np.sum, sk.transform.rescale (for multiscale)


def align(image1, image2):
    window = 15
    best_score = -np.inf
    best_dx, best_dy = 0, 0
    h, w = image2.shape
    margin_h, margin_w = int(h * 0.1), int(w * 0.1)
    image2_norm = image2[margin_h:h - margin_h, margin_w:w - margin_w]
    image2_norm = (image2_norm - np.mean(image2_norm)) / np.linalg.norm(image2_norm - np.mean(image2_norm))
    for dy in range(-window, window + 1):
        for dx in range(-window, window + 1):
            shifted = np.roll(image1, (dy, dx), axis=(0, 1))
            image1_norm = shifted[margin_h:h - margin_h, margin_w:w - margin_w]
            image1_norm = (image1_norm - np.mean(image1_norm)) / np.linalg.norm(image1_norm - np.mean(image1_norm))
            ncc = np.sum(image1_norm * image2_norm)
            if ncc > best_score:
                best_score = ncc
                best_dx, best_dy = dx, dy
    print((best_dx, best_dy))
    return np.roll(image1, (best_dy, best_dx), axis=(0, 1))


def pyramid(image1, image2, min_size=64, window=15, dy_guess=0, dx_guess=0, top_level=True):
    h, w = image2.shape
    if min(h, w) > min_size:
        small1 = rescale(image1, 0.5, anti_aliasing=True)
        small2 = rescale(image2, 0.5, anti_aliasing=True)
        dy_guess, dx_guess = pyramid(small1, small2, min_size, window, dy_guess, dx_guess, top_level=False)
        dy_guess, dx_guess = dy_guess * 2, dx_guess * 2
        window = 2
    best_score = -np.inf
    best_dx, best_dy = dx_guess, dy_guess
    margin_h, margin_w = int(h * 0.1), int(w * 0.1)
    image2_norm = image2[margin_h:h - margin_h, margin_w:w - margin_w]
    image2_norm = (image2_norm - np.mean(image2_norm)) / np.linalg.norm(image2_norm - np.mean(image2_norm))
    for dy in range(dy_guess - window, dy_guess + window + 1):
        for dx in range(dx_guess - window, dx_guess + window + 1):
            shifted = np.roll(image1, (dy, dx), axis=(0, 1))
            image1_norm = shifted[margin_h:h - margin_h, margin_w:w - margin_w]
            image1_norm = (image1_norm - np.mean(image1_norm)) / np.linalg.norm(image1_norm - np.mean(image1_norm))
            ncc = np.sum(image1_norm * image2_norm)
            if ncc > best_score:
                best_score = ncc
                best_dx, best_dy = dx, dy
    if top_level:
        print((best_dx, best_dy))
        return np.roll(image1, (best_dy, best_dx), axis=(0, 1))
    return best_dy, best_dx


ag = pyramid(g, b)
ar = pyramid(r, b)
# create a color image
im_out = np.dstack([ar, ag, b])

# save the image
fname = f'output/{file_name}.jpg'
skio.imsave(fname, sk.img_as_ubyte(im_out))

# display the image
skio.imshow(im_out)
skio.show()