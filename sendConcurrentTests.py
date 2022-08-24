import requests
from concurrent.futures import ThreadPoolExecutor

def get_url(url):
    return requests.get(url)

list_of_urls = ["http://192.168.0.37:49154"]*10000

with ThreadPoolExecutor(max_workers=10) as pool:
    response_list = list(pool.map(get_url,list_of_urls))

for response in response_list:
    if response.status_code != 200:
        print("missed connection")
    # print(response.status_code)