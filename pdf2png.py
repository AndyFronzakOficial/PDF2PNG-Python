#Importar 
import fitz 
from PIL import Image

#Script
input_pdf_path = 'cv.pdf' #vai ate o arquivo
pdf_document = fitz.open(input_pdf_path) #abre o arquivo
page = pdf_document.load_page(0)   #vai na primeira pagina
pix = page.get_pixmap() #
image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
output_png_path = 'meu curriculo.png'
image.save(output_png_path)

pdf_document.close()

image.show()
