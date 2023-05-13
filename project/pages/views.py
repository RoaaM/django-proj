from django.shortcuts import render
from  . import ocr
import os
from django.shortcuts import redirect, render  
from django.http import HttpResponse  
# from .ocr import extract_text
from django.shortcuts import render
from google.cloud import vision
from django.conf import settings
from .forms import ImageForm
from google.cloud.vision_v1 import types
# Set path to Google Cloud credentials JSON file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\roaas\Documents\roaa_workspace\django-proj\lowproject-385216-f98896a4a2e9.json"

# Create a client for the Google Cloud Vision API

# Create your views here.
# we connect views with templets and with models(database)
# dtl for templets 
# dtl--> django templets languages

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    data = {'name':'roaa',
             'age':'24'}
    return render(request, 'pages/about.html', data)



def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            # send image to Cloud Vision API
            client = vision.ImageAnnotatorClient()
            content = image.image.read()
            image_binary = types.Image(content=content)
            response = client.document_text_detection(image=image_binary)
            image.text = response.full_text_annotation.text
            print(f"image: {image}")
            image.save()
            return render(request, 'pages/index.html', {'form': form, 'text': image.text})
    else:
        form = ImageForm()
    return render(request, 'pages/index.html', {'form': form})
