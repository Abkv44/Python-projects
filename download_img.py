# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:14:23 2024

@author: Abk
"""

import argparse
import requests

def img_downloader():
    parser = argparse.ArgumentParser(description= "image downloader with given url")
    parser.add_argument("url", type=str)
    parser.add_argument("-d", "--download")
    args = parser.parse_args()
    
    result = args.url
    download_file(result)
    print("Downloaded!")
    
def download_file(url):
    local_filename = url.split('/')[-1]
    local_filename = input("Enter file name to save with extension name:")
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

url = "https://imagej.net/images/LineGraph2.jpg"

local_filename = url.split('.')[-1]

print(local_filename)
# print(type(local_filename))
download_file(url)

print("File downloaded! hurray!")
# img_downloader()


