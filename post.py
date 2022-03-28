import requests
import time
import sys


def post(file, layer, shape):
    intermediate_features = file
    size = sys.getsizeof(intermediate_features)
    upload_url = "http://httpbin.org/post"

    #start = time.time()
    ## post
    res = requests.post(upload_url, files= {'form_field_name': intermediate_features})

    elapsed_time = res.elapsed.total_seconds()
    #finish = time.time()

    if res.ok:
        print(f'For layer {layer} :\nShape : {shape} Size: {size} bytes\nStatus : {res}  Time Taken: {elapsed_time} seconds\n')
    else:
        print('Some error!!')