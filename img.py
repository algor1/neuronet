from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
import tensorflow as tf
from PIL import Image, ImageDraw



image1 = Image.new("L",(28,28),color=255)  
draw = ImageDraw.Draw(image1)  
width =28
height =28
for k in range(1,2):
  for i in range(0,width):
    fff=str(i)
    for j in range(0,height):
      col= int(255*(1-mnist.test.images[k,i*28+j]))
      if col>128:
        fff=fff+"0"
      else:
        fff=fff+"-"
      draw.point((j, i),fill=col)
    print (fff)
  image1.show()
print (mnist.test.images[1,],i,j)
print (len(mnist.test.images),i,j)


from PIL import Image
image = Image.open("0.jpg")  
image2=image.resize((28,28))
image2.show()
pix= image2.load()
k=1
for i in range(0,width):
  fff=str(i)
  for j in range(0,height):
    a = pix[i, j][0]
    b = pix[i, j][1]
    c = pix[i, j][2]
    col = (a + b + c)//3
    mnist.test.images[k,i*28+j]=col/255
    if col>128:
      fff=fff+"0"
    else:
      fff=fff+"-"
    draw.point((j, i),fill=col)
  print (fff)


image1.show()


