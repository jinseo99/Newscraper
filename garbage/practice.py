from bs4 import BeautifulSoup
#import requests
import pathlib
import os

"""
fn = os.path.join(os.path.dirname(__file__), 'html_files/Galaxy Note 20+ ‘Final’ Design Reveals Stunning New Display.htm')
source = requests.get('').text
soup = BeautifulSoup(source, 'lxml')
with open(fn) as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


article = soup.find('div', class_='article-body fs-article fs-responsive-text current-article')

article_text = "" 
for summary in article.find_all('p'):
    article_text+=summary.text

print(article_text)
"""


def writeText(file_name, article_text):
    with open(file_name, "w") as text_file: 
        text_file.write(article_text)

import urllib.request
url = "https://news.google.com/?hl=en"
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'

headers = {'User-Agent': user_agent}


results = []
deamplify = False

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
page = response.read()
content = BeautifulSoup(page, "html.parser")
content = content.find("h2").parent.parent.parent
result = content.findChildren("div", recursive=False)
section = None
for item in result:
    try:
        try:
            section = item.find("h2").find("a").text
        except Exception as sec_e:
            pass
        title = item.find("h3").text
        if deamplify:
            try:
                link = item.find("article").get("jslog").split('2:')[1].split(';')[0]
            except Exception as deamp_e:
                print(deamp_e)
                link = 'news.google.com/' + item.find("h3").find("a").get("href")
        else:
            link = item.find("h3").find("a").get("href")
        try:
            datetime = item.find("time").get("datetime")
        except:
            datetime = None
        try:
            time = item.find("time").text
        except:
            time = None
        try:
            site = item.find("time").parent.find("a").text
        except:
            site = None
        try:
            img = item.find("img").get("src")
        except:
            img = None
        desc = None
        if link.startswith('https://www.youtube.com/watch?v='):
            desc = 'video'

        results.append(
            {'section': section,
                'title': title,
                'datetime': datetime,
                'time': time,
                'site': site,
                'desc': desc,
                'link': link,
                'media': None,
                'img': img})
        a = True
        for key in results[0].keys():
            print(key, " ", results[0][key])    
        if a:
            break   
    except Exception as big_e:
        pass
response.close()

