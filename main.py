import qr_generator
import qrcode

def start(text1,passw):
    inp = text1
    link = qr_generator.qr_generate(inp,passw)
    return link
