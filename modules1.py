import img2pdf
image = "/home/dheenadhayalan/python_class/test.jpg"
output = "/home/dheenadhayalan/python_class/test.pdf"

with open(output,'wb') as f:
	f.write(img2pdf.convert(image))
	f.close()
