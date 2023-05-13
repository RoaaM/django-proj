# import os
# import re
# from google.cloud import vision
# from django.shortcuts import render

# # Set path to Google Cloud credentials JSON file
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\roaas\Documents\roaa_workspace\django-proj\lowproject-385216-f98896a4a2e9.json"

# # Create a client for the Google Cloud Vision API
# client = vision.ImageAnnotatorClient()

# # Define a function to extract text from an image using Google Cloud Vision API
# def extract_text(image):
#     image = vision.Image(content=image)
#     response = client.text_detection(image=image)
#     text = response.text_annotations[0].description.strip()
#     # Remove any non-alphanumeric characters and extra whitespace
#     text = re.sub('[^0-9a-zA-Z \n]+', '', text).strip()
#     return text
