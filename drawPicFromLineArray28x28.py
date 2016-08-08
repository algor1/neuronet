from PIL import Image, ImageDraw
import numpy as np

def drawPicture28x28(pix3):
  image3 = Image.new("RGB",(28,28),color=(255,255,255))  
  draw3 = ImageDraw.Draw(image3)  
  if min(pix3)>=0:
    kBlue=0
  else:
    kBlue=-255/min(pix3)
  if max(pix3)<=0:
    kRed=0
  else:
    kRed=255/max(pix3)
    
  print (max(pix3), min(pix3))
  
  for i in range(0,28):
    for j in range(0,28):
      x=i*28+j
      if pix3[x]>0:
        colR=int((pix3[x])*kRed)
        colB=0
      else:
        colB=int((pix3[x])*kBlue)
        colR=0
      draw3.point((i, j),fill=(colR,0,colB))
  return image3
  #image3.show()

#массив из n линейниых массивов784
def drawBunchOfPicture28x28(doubleArray784):
  #print(doubleArray784)
  imageout = Image.new("RGB",(len(doubleArray784)*28,28),color=(255,255,255))  
  for i in range(len(doubleArray784)):
    imageout.paste(drawPicture28x28(doubleArray784[i]),box=(i*28,0))
  return imageout


  


#добываем картинку
#pix33=sess.run(W)
#или
inputSubArray=[]
pix33=[]
nnn=0

for i in range (784):
  if i == nnn:
    nnn+=29
    inputSubArray.append([1,1,1,1,1,1,1,1,1,1])
  else:
    inputSubArray.append([0,0,0,0,0,0,0,0,0,0])
pix33=inputSubArray
print(len(pix33[2]))

def drawWeights(W):
  outputPixArray=[]
  for k in range(10):
    for i in range (784):
      outputPixArray.append(W[i][k])
    drawPicture28x28(outputPixArray)
