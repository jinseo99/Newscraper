import requests
from bs4 import BeautifulSoup
import time 
import pandas as pd
from goose3 import Goose
from Unbuffered import Unbuffered
import sys
from nltk.tokenize import RegexpTokenizer
import os


sys.stdout = Unbuffered(sys.stdout)

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
headers = {'User-Agent': user_agent}
df = pd.DataFrame(pd.read_csv('csv_files/googlenews_results_03+49_06-04-2020.csv'))
url_lists = df['link']

def save_csv(index, save_file_path):
    tmp = pd.DataFrame(df.iloc[[index]])

    if (not os.path.isfile(save_file_path)):
        tmp.to_csv(save_file_path, index=False, mode = 'w')
        return
    tmp.to_csv(save_file_path, index=False, mode = 'a', header=False)


save_path = "csv_files/tesla_06-29-2010_08-10-2015.csv"
tokenizer = RegexpTokenizer(r'\w+')
keyword = 'tesla'
delete_row_ind =[]
for i, url in enumerate(url_lists):
    print ("currently on index", i, url)
    req = requests.get(url, time.sleep(3), headers=headers)
    extractor = Goose()
    article = extractor.extract(raw_html=req.content)
    text = tokenizer.tokenize(article.cleaned_text.lower())
    keyword_count=0
    for word in text:
        if word == keyword:
            keyword_count+=1
            
    if keyword_count < 5:
        print('deleted')
        delete_row_ind.append(i)
    else:
        save_csv(i, save_path)
        
