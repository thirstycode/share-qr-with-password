import qr_generator
import qrcode
from PIL import Image


inp = input("Text To Store : ")
img = qr_generator.qr_generate(inp)
img.save("p.Bmp")
img.show()
