import qrcode
from support.link_generate import generate as l_g

def qr_generate(text,passw):
    (link,id) = l_g(text,passw)
    img = qrcode.make(link)
    img.save("qrstore" + "\\" + "qrimage" + ".Bmp")
    return link
