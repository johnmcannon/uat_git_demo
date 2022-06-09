import ssl
import astropy
import numpy as np
import skimage.io
from astropy import units as u
import skimage.io
from matplotlib import pyplot as plt
# Optical image of a neat galaxy:
width=2000
height=2000
pixelsize=0.396
ra=152.11717
dec=12.30650
gsize=0.5
scale=pixelsize*gsize
url="http://skyservice.pha.jhu.edu/DR12/ImgCutout/getjpeg.aspx?ra="+str(ra)
url+="&dec="+str(dec)+"&scale="""+str(scale)+"&width="+str(width)
url+="&height="+str(height)+"&opt=G"
img=skimage.io.imread(url)
plt.imshow(img)
plt.tight_layout()
plt.axis('off')
plt.show()


