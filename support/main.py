import support.qr_generator

def start(text1,passw):
    inp = text1
    link = qr_generator.qr_generate(inp,passw)
    return link
