"""
WebScraper.py for web scraping
"""
from datetime import timedelta, date, datetime
from GoogleNews import GoogleNews
import pandas as pd
import os.path

class WebScraper:
    def __init__(self):
        self.__results = [] # {'title': tmp_text, 'media': tmp_media,'date': tmp_date,'desc': tmp_desc, 'link': tmp_link,'img': tmp_img}

    def _save_csv(self, save_file_path, googlenews):
        df = pd.DataFrame(googlenews.results())
        print("saved rows ",df.shape[0])

        if (not os.path.isfile(save_file_path)):
            df.to_csv(save_file_path, index=False, mode = 'w')
            googlenews.clear()
            return
        df.to_csv(save_file_path, index=False, mode = 'a', header=False)
        googlenews.clear()

    def _daterange(self):
        for n in range(int ((self.__end - self.__start).days+1)):
            yield self.__start + timedelta(n)

    def setListofDates(self, start, end):
        self.__start = start
        self.__end = end
        self.__all_date = []
        for single_date in self._daterange():
            self.__all_date.append(single_date.strftime("%m/%d/%Y"))
        print(self.__all_date[-1])


    def scrapAllPages(self, googlenews, save_file_path=""):
        for cur_date in self.__all_date:
            print("The current date searching ",cur_date)
            googlenews.setTimeRange(cur_date, cur_date)

            page_counter = 1
            while True:
                if(not googlenews.search(page_counter)):
                    print("last page is ", str(page_counter - 1))
                    break
                if save_file_path:
                    self._save_csv(save_file_path, googlenews)
                page_counter += 1 
