#pillow interface is used to edit images/media 

from PIL import Image

def resize_image(size1,size2):
    image=Image.open("D:\pythonproblems\img\size.png")
    print (image.size)

    resize_image=image.resize((size1,size2))
    resize_image.save('resized'+str(size2)+'.jpeg')


size1=int(input("Enter width:"))
size2=int(input("Enter Length:"))
resize_image(size1,size2)