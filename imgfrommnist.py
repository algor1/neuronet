from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

from drawPicFromLineArray28x28 import drawPicture28x28 as drpic
from drawPicFromLineArray28x28 import drawBunchOfPicture28x28 as drbanch
import numpy as np

from PIL import Image, ImageDraw

p=mnist.test.images
l=mnist.test.labels
m0=[]
m1=[]
m2=[]
m3=[]
m4=[]
m5=[]
m6=[]
m7=[]
m8=[]
m9=[]
for i in range(100):
    if l[i][0]==1:
       # print(p[i])
        m0.append(p[i].tolist())
    elif l[i][1]==1:
        m1.append(p[i])
    elif l[i][2]==1:
        m2.append(p[i])
    elif l[i][3]==1:
        m3.append(p[i])
    elif l[i][4]==1:
        m4.append(p[i])
    elif l[i][5]==1:
        m5.append(p[i])
    elif l[i][6]==1:
        m6.append(p[i])
    elif l[i][7]==1:
        m7.append(p[i])
    elif l[i][8]==1:
        m8.append(p[i])
    elif l[i][9]==1:
        m9.append(p[i])
#print (m0)
drbanch(m0).show
