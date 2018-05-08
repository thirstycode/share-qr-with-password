import pdf
from config import domain_url
from config import location
import random

def generate(text,passw):
    domain = domain_url + "/"
    unique_id = random.choice(range(1,1000000000))
    url = pdf.make_pdf(text,unique_id,passw)
    return (url,unique_id)
