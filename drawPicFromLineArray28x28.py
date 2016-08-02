def drawPicture(pix3):
  image3 = Image.new("RGB",(28,28),color=(255,255,255))  
  draw3 = ImageDraw.Draw(image3)  
  kBlue=-255/min(pix3)
  kRed=255/max(pix3)
  print (max(pix3), min(pix3))
  
  for i in range(0,28):
    for j in range(0,28):
      if pix3[i*28+j,4]>0:
        colR=int(pix3[i*28+j,4]*kRed)
        colB=0
      else:
        colB=int(pix3[i*28+j,4]*kBlue)
        colR=0
      draw3.point((i, j),fill=(colR,0,colB))
  image3.show()


#добываем картинку
pix33=sess.run(W)
#или
inputSubArray=[]
nnn=0
for i in range (784):
  if i == nnn:
    nnn+=29
    inputSubArray.append(1)
  else:
    inputSubArray.append(0)
print(inputSubArray)

print(len(pix33))
for k in range(10):
  for i in range (784):
    outputpixarray[i]=pix33[i,k]
  drawPicture(outputPixArray)
