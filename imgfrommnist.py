#from tensorflow.examples.tutorials.mnist import input_data
#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

from drawPicFromLineArray28x28 import drawPicture28x28 as drpic
from drawPicFromLineArray28x28 import drawBunchOfPicture28x28 as drbanch

from PIL import Image, ImageDraw

p=mnist.test.images
l=mnist.test.labels
for i in range(100):
    if l[i]==[1,0,0,0,0,0,0,0,0,0]:
        m0.append(p[i])
    elif l[i]==[0,1,0,0,0,0,0,0,0,0]:
        m1.append(p[i])
    elif l[i]==[0,0,1,0,0,0,0,0,0,0]:
        m2.append(p[i])
    elif l[i]==[0,0,0,1,0,0,0,0,0,0]:
        m3.append(p[i])
    elif l[i]==[0,0,0,0,1,0,0,0,0,0]:
        m4.append(p[i])
    elif l[i]==[0,0,0,0,0,1,0,0,0,0]:
        m5.append(p[i])
    elif l[i]==[0,0,0,0,0,0,1,0,0,0]:
        m6.append(p[i])
    elif l[i]==[0,0,0,0,0,0,0,1,0,0]:
        m7.append(p[i])
    elif l[i]==[0,0,0,0,0,0,0,0,1,0]:
        m8.append(p[i])
    elif l[i]==[0,0,0,0,0,0,0,0,0,1]:
        m9.append(p[i])

drbanch(m0).show
