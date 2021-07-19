#!/usr/bin/env python3

import requests # to get image from the web
import shutil # to save it locally
import os
import pyperclip

## Set up the image URL and filename
with open('downloads') as f: s = f.read()
counter = 0
urls = s.split("\n")
for image_url in urls:
    counter += 1
    filename = "image"+str(counter)+".png"

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print(filename)
        pyperclip.copy(filename)
        os.system("gruvbox-factory")

    else:
        print('Image Couldn\'t be retreived')
