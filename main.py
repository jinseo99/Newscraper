"""
main.py for web scraping
essential libraries:
    WebScraper.py
    myGoogleNews.py
    Unbuffered.py
start date: 2010, 6, 29
"""

from WebScraper import WebScraper
from myGoogleNews import myGoogleNews
from datetime import timedelta, date, datetime
from Unbuffered import Unbuffered
import sys

googlenews = myGoogleNews(key="tesla")
webscraper = WebScraper()
sys.stdout = Unbuffered(sys.stdout)

start_date = date(2015, 8, 11)

end_date = date.today()

save_file_name = datetime.now().strftime("googlenews_results_%H+%M_%m-%d-%Y")
save_file_name = "csv_files/" + save_file_name + '.csv'

### start test case ### 
#end_date = date(2015, 8, 13)
#save_file_name = ""
### end test case ###

webscraper.setListofDates(start_date, end_date)
webscraper.scrapAllPages(googlenews, save_file_name)