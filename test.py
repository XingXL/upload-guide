#!/usr/bin/python
#coding:utf-8
from PIL import Image
import numpy as np
import scipy.misc
from scipy.misc import imsave
import numpy as np, os, sys
import matplotlib.pyplot as plt
import pylab

def get_img(src, img_size=False):
   img = scipy.misc.imread(src, mode='RGB') # misc.imresize(, (256, 256, 3))
   if not (len(img.shape) == 3 and img.shape[2] == 3):
       img = np.dstack((img,img,img))
   if img_size != False:
       img = scipy.misc.imresize(img, img_size)
   return img

target_o = get_img('005.png')
plt.imshow(target_o)
plt.show()
target_shape = (1,) + target_o.shape
print(target_shape)
target = Image.fromarray(target_o)
imsave('zx.png',target)
