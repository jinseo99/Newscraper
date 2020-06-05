# 1. search google for 'tesla', specifying the dates.
# 2. download all pages from specified date into texts then summarize.
# 3. table of summaries of texts for each date

import pickle
from datetime import timedelta, date, datetime
from GoogleNews import GoogleNews
import pandas as pd
import os.path

class WebScraper:
    def __init__(self):
        self.titles = []
        self.links = []
        self.results = [] # {'title': tmp_text, 'media': tmp_media,'date': tmp_date,'desc': tmp_desc, 'link': tmp_link,'img': tmp_img}

    def copy_googlenews_results(self, googlenews):
        self.titles = self.titles + googlenews.gettext()
        self.links = self.links + googlenews.get__links()
        self.results = self.results + googlenews.result()
        googlenews.clear()

    def save_csv(self, save_file_name, googlenews):
        df = pd.DataFrame(googlenews.result())
        print("number of rows ",df.shape[0])

        if (not os.path.isfile(save_file_name)):
            df.to_csv(save_file_name, index=False, mode = 'w')
            googlenews.clear()
            return
        df.to_csv(save_file_name, index=False, mode = 'a', header=False)
        googlenews.clear()

    def save_pickle(self):
        now = datetime.now()
        now = now.strftime("googlenews_%H+%M+%S_%m-%d-%Y")
        save_file_name = now +".pickle"

        with open(save_file_name, "wb") as fp:
            pickle.dump(self.titles, fp)
            pickle.dump(self.links, fp)
            pickle.dump(self.results, fp)
        print("files saved on", save_file_name)
    
    def load(self, load_file_name):

        with open(load_file_name, "rb") as fp:
            self.titles = pickle.load(fp)
            self.links = pickle.load(fp)
            self.results = pickle.load(fp)

# start date 06/29/2010
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2010, 6, 29)
end_date = date.today()

all_date = []
for single_date in daterange(start_date, end_date):
    all_date.append(single_date.strftime("%m/%d/%Y"))
    
googlenews = GoogleNews()
googlenews.setlang('en')

webscraper = WebScraper()

now = datetime.now()
save_file_name = now.strftime("googlenews_results_%H+%M_%m-%d-%Y")
save_file_name = save_file_name + '.csv'

count = 0
for cur_date in all_date:
    print("The current date searching ",cur_date)
    googlenews.setTimeRange(cur_date, cur_date)

    googlenews.search('tesla')
    webscraper.save_csv(save_file_name, googlenews)

    page_counter = 2
    while True:
        googlenews.getpage(page_counter)
        if(not googlenews.result()):
            print("last page is ", str(page_counter - 1))
            break
        webscraper.save_csv(save_file_name, googlenews)
        page_counter += 1 
    
    if count == 1:
        break
    count+=1


#webscraper.save()