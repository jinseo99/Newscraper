import requests

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
headers = {'User-Agent': user_agent}

test_url = "https://wallstreetpit.com/36356-the-real-yield-curve-and-a-double-dip-recession/"
response = requests.get(url=test_url, headers=headers, verify=False)
print(response.text)
