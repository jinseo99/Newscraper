from bs4 import BeautifulSoup
import requests
import urllib.request

res = requests.get("https://www.google.com/search?q=tesla&lr=lang_en&tbs=lr:lang_1en&tbm=nws&start=0", stream =True)

"""
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
headers = {'User-Agent': user_agent}
req = urllib.request.Request("https://www.google.com/search?q=tesla&lr=lang_en&tbs=lr:lang_1en&tbm=nws&start=0", headers=headers)
response = urllib.request.urlopen(req)
page = response.read()
"""

print(res.raw)
#soup = BeautifulSoup(res.text, 'html.parser')
#with open("test.txt", 'w') as t:
#    t.writelines(res.raw.read())
