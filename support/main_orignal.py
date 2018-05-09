import support.qr_generator
from PIL import Image


inp = input("Text To Store : ")
img = qr_generator.qr_generate(inp)
img.save("p.Bmp")
print("qr saved as p.bmp")
img.show()
