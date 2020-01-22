from __future__ import print_function
import requests
import json
import sys
from time import perf_counter

addr = 'http://10.138.0.53:5000'

endpoint = sys.argv[1]
num_iterations = sys.argv[2]
n = int(num_iterations)


headers = {'content-type': 'image/png'}
headers1 ={'content-type':'text/plain'}
img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
# send http request with image and receive response
image_url = addr + '/api/image'
number_url = addr + '/api/add/2/3'
if(endpoint == 'image'):
    count = 1
    t1_start = perf_counter()
    while(count<=n): 
        response = requests.post(image_url, data=img, headers=headers)
        print(json.loads(response.text))
        print("Response is", response)
        count = count+1
    t1_stop = perf_counter()
    total_time = t1_stop - t1_start
    time_per_query = total_time/n
    print(time_per_query)
else:
    count = 1
    t1_start = perf_counter()
    while(count<=n): 
        response1 = requests.get(number_url, headers=headers1)
        print(response1)
        count = count+1
    t1_stop = perf_counter()
    total_time = t1_stop - t1_start
    time_per_query = total_time/n
    print(time_per_query)




#print(json.loads(response.text))




#print(json.loads(response1.text))


