import requests
from bs4 import BeautifulSoup
import time 
from retrying import retry
class myGoogleNews:
    def __init__(self, lang="en", key="", start="",end=""):
        self.__results = []
        self.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
        self.headers = {'User-Agent': self.user_agent}
        self.__lang = lang
        self.__start = start
        self.__end = end
        self.__key = key

    def setlang(self, lang):
        self.__lang = lang

    def setTimeRange(self, start, end):
        self.__start = start
        self.__end = end
    
    def setkey(self,key):
        self.__key = "+".join(self.__key.split(" "))
    
    def results(self):
        return self.__results

    def _getSearchLink(self, page = 1):
        if self.__start != "" and self.__end != "":
            self.url = "https://www.google.com/search?q={}&lr=lang_{}&tbs=lr:lang_1{},cdr:1,cd_min:{},cd_max:{}&tbm=nws&start={}".format(self.__key,self.__lang,self.__lang,self.__start,self.__end,(10 * (page - 1)))
        else:
            self.url = "https://www.google.com/search?q={}&lr=lang_{}&tbs=lr:lang_1{}&tbm=nws&start={}".format(self.__key,self.__lang,self.__lang,(10 * (page - 1))) 

    def clear(self):
        self.__results=[]

    def _lastpage(self):
        return
    def search(self, page = 1):
        self._getSearchLink(page)
        try:
            self.req = requests.get(self.url, time.sleep(4), headers=self.headers)
            self.page = self.req.text
            self.content = BeautifulSoup(self.page, "html.parser")


            result = self.content.find_all("div", class_="g")
            if not result:
                return False

            for item in result:
                try:
                    tmp_text = item.find("h3").text
                except Exception:
                    tmp_text = ''
                try:
                    tmp_link = item.find("h3").find("a").get("href")
                except Exception:
                    tmp_link = ''
                try:
                    tmp_media = item.find("h3").findNext('div').find_all("span")[0].text
                except Exception:
                    tmp_media = ''
                try:
                    tmp_date = item.find("h3").findNext('div').find_all("span")[2].text
                except Exception:
                    tmp_date = ''
                try:
                    tmp_desc = item.find("div", class_="st").text
                except Exception:
                    tmp_desc = ''
                try:
                    tmp_img = item.find("img").get("src")
                except Exception:
                    tmp_img = ''
                self.__results.append({'title': tmp_text, 'media': tmp_media,'date': tmp_date,'desc': tmp_desc, 'link': tmp_link,'img': tmp_img})
            self.req.close()
            return True
        except Exception as exc:
            print(exc)
            self.search()



    
