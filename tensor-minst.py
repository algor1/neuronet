from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
import tensorflow as tf
from PIL import Image, ImageDraw

x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
saver = tf.train.Saver()
saver.restore(sess, "model.ckpt")
print("Model restored.")
##for i in range(100000):
##  batch_xs, batch_ys = mnist.train.next_batch(100)
##  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


from PIL import Image
image = Image.open("3.jpg")  
image2=image.resize((28,28))
image2.show()
image1 = Image.new("L",(28,28),color=255)  
draw = ImageDraw.Draw(image1) 
pix= image2.load()
piix=(list())
k=1

for i in range(0,28):
  for j in range(0,28):
    a = pix[i, j][0]
    b = pix[i, j][1]
    c = pix[i, j][2]
    col = (a + b + c)//3
    piix.append(col/255)
    draw.point((i, j),fill=col)

piix1=[piix]
image1.show()


#print(sess.run(y,feed_dict={x:    mnist.test.images}))
ans=sess.run(y,feed_dict={x: piix1})

for i in range(len(ans[0])):
  print (i," - вероятность ", round(ans[0,i]*100,2), "%")


def drawPicture(pix3):
  colR=0
  colB=0
  image3 = Image.new("RGB",(28,28),color=(255,255,255))  
  draw3 = ImageDraw.Draw(image3)   
  for i in range(0,28):
    for j in range(0,28):
      print (max(pix3), min(pix3))
      if int(pix3[i*28+j,4]*255)>0:
        colR=int(pix3[i*28+j,4]*255)
        colB=0
      else:
        colB=-int(pix3[i*28+j,4]*255)
        colR=0
      draw3.point((i, j),fill=(colR,colR,colR))
  image3.show()

pix33=sess.run(W)
print(len(pix33))
drawPicture(pix33)

