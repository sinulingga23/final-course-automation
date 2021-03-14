
#!/usr/bin/python3

import os
import requests


def upload_images():
  images_name = os.listdir('supplier-data/images')
  for image in images_name:
    if ".jpeg" in image:
      url = "http://35.232.249.130/upload/"
      with open('supplier-data/images/'+image, 'rb') as opened:
        response = requests.post(url, files={'file': opened})
        if response.ok is False:
          print(response.raise_for_status())
      opened.close()

def main():
  upload_images()

if __name__ == "__main__":
  main()

