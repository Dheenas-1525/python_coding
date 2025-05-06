import img2pdf
from PIL import Image
import os
file_name = input("enter the image name : ")
image = Image.open(file_name)
with open(file_name,'wb') as file:
    file.write(img2pdf.convert(file_name))
Image.close()
file.close()
print("successfully generated pdf ")


 
