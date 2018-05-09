from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from config import owner_pass
from config import location
import support.share


def make_pdf(text,id,passw):
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(10, 550,str(text))
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("download1.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    output_name = location + "" + "database" + "\\" + "protected" + str(id) + ".pdf"
    outputStream = open(output_name, "wb")
    output.encrypt(passw, owner_pass, use_128bit=True)
    output.write(outputStream)
    outputStream.close()
    url = share.upload(output_name,"/" + "protected" + str(id) + ".pdf")
    return url
