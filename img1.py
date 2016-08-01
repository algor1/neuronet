from PIL import Image
image = Image.open("0.jpg")  
image2=image.resize((28,28))
image2.show()
print(list(image2.load()))
