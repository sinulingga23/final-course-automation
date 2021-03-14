#!/usr/bin/python3
from PIL import Image
import os


def change_images():
  images_name = os.listdir('supplier-data/images')
  for image in images_name:
   if ".tiff" in image:
     ext = image.split('.')
     current_image = Image.open('supplier-data/images/'+image)
     width, height = current_image.size;
     if width >= 3000 and height >= 2000:
       current_image.convert("RGB").resize((600,400)).save("supplier-data/images/"+ext[0]+".jpeg")

def main():
  change_images()

if __name__ == "__main__":
  main()
