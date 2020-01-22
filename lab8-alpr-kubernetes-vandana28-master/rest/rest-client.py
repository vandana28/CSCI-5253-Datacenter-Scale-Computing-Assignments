#!/usr/bin/env python

# importing the required libraries
import requests
import sys

# storing the values for future use
addr = 'http://{}:5000'
filename = sys.argv[2]
img = open(filename, 'rb').read()
headers = {'content-type': 'image/jpg'}


def getImageSize():
    image_url = addr + '/api/image/' + str(filename)
    # generate request for image
    response = requests.post(image_url, data=img, headers=headers)
    print(response.text)


addr = addr.format(sys.argv[1])

getImageSize()
print("Image handled")