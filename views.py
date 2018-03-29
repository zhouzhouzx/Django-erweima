# Create your views here.
from __future__ import unicode_literals
from django.http import HttpResponse
import qrcode
from django.utils.six import BytesIO
from django.shortcuts import render
from urllib.parse import urlencode
from urllib.request import unquote,quote

def home(request):
    return render(request,'index.html')


def generate_qrcode(request):
     qr = qrcode.QRCode(
          version=5,
          error_correction=qrcode.constants.ERROR_CORRECT_M,
          box_size=10,
          border=4,
     )

     website = request.GET['website']
     qr.add_data(website)
     qr.make(fit=True)
     img = qr.make_image(fill_color="black", back_color="white")
     buf = BytesIO()
     img.save(buf)
     image_stream = buf.getvalue()
     response = HttpResponse(image_stream, content_type="image/png")
     return response
