#!/usr/bin/python3

import os
import requests

def post_description_fruits():
  descriptions = os.listdir('supplier-data/descriptions')

  for desc in descriptions:
    ext = desc.split('.')
    fruit = {}
    with open('supplier-data/descriptions/'+desc, mode='r') as opened:
      temp = opened.readlines()
      fruit["name"] = temp[0].rstrip("\n")
      fruit["weight"] = int(temp[1].split(' ')[0])
      fruit["description"] = temp[2].rstrip("\n")
      fruit["image_name"] = ext[0] + ".jpeg"
      opened.close()
    response = requests.post('http://35.232.249.130/fruits/', data=fruit)
    if not response.ok:
     print(response.raise_for_status())

def main():
  post_description_fruits()

if __name__ == "__main__":
  main()

