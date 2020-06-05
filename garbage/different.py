"""
Testing different requests functions:
    urllib
    requests

save html text files in directory: test_html/
link to compare: https://www.google.com/search?q=tesla&lr=lang_en&tbs=lr:lang_1en,cdr:1,cd_min:06/29/2010,cd_max:06/29/2010&tbm=nws&start=0
"""
from bs4 import BeautifulSoup
import urllib.request
import requests
import urllib3

class Different:
    def __init__(self, test_url, directory):
        self.test_url = test_url
        self.directory = directory
    def first_source(self):
        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(self.test_url, headers=headers)
        response = urllib.request.urlopen(req)
        page = response.read()
        with open((self.directory+"test1.txt"), 'w') as wf:
            wf.writelines(str(page))

    def first_html(self):

        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(self.test_url, headers=headers)
        response = urllib.request.urlopen(req)
        page = response.read()
        content = BeautifulSoup(page, "html.parser")

        with open((self.directory+"test1_2.txt"), 'w') as wf:
            wf.writelines(content.prettify())

    def second_source(self):
        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
        headers = {'User-Agent': user_agent}

        req = requests.get(self.test_url, headers=headers)
        page = req.text
        with open((self.directory+"test2.txt"), 'w') as wf:
            wf.writelines(page)

    def second_html(self):
        user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
        headers = {'User-Agent': user_agent}

        req = requests.get(self.test_url, headers=headers)
        page = req.content
        content = BeautifulSoup(page, "html.parser")
        with open((self.directory+"test2_2.txt"), 'w') as wf:
            wf.writelines(content.prettify())

    def third_source(self):
        req = urllib3.PoolManager()
        response = req.request('GET', self.test_url)

        page = response.data.decode('ISO-8859-1')
        with open((self.directory+"test3.txt"), 'w') as wf:
            wf.writelines(page)

    def third_html(self):
        req = urllib3.PoolManager()
        response = req.request('GET', self.test_url)

        page = response.data.decode('ISO-8859-1')
        content = BeautifulSoup(page, "html.parser")
        with open((self.directory+"test3_2.txt"), 'w') as wf:
            wf.writelines(content.prettify())
    
    def search_html(self, content):
        result = content.find_all("div", class_="g")
        print (result)
directory = 'test_html/'
test_url = "https://www.google.com/search?q=tesla&lr=lang_en&tbs=lr:lang_1en,cdr:1,cd_min:08/10/2015,cd_max:08/10/2015&tbm=nws&start=20"

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
headers = {'User-Agent': user_agent}

req = requests.get(test_url, headers=headers)
page = req.content
content = BeautifulSoup(page, "html.parser")
result = content.find_all("div", class_="g")
print(result)

#different = Different(test_url, directory)
#different.second_html()