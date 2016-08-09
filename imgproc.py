#Writing an array to a file:

from scipy import misc

f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()


#Creating a numpy array from an image file:

from scipy import misc
face = misc.face()
misc.imsave('face.png', face) # First we need to create the PNG file

face = misc.imread('face.png')
type(face)      

#face.shape, face.dtype
#((768, 1024, 3), dtype('uint8'))
#dtype is uint8 for 8-bit images (0-255)
