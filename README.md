# Website Scraper

Website Scraper is a group of Python libraries with the intent of scraping news articles for summaries.

## Usage

more details in main.py

'''python
from WebScraper import WebScraper
from myGoogleNews import myGoogleNews

googlenews = myGoogleNews(key="Google") # searches 'Google' in google news
webscraper = WebScraper()

webscraper.setListofDates(start_date='06/01/1999', end_date='06/01/2000')
webscraper.scrapAllPages(googlenews, save_file_path='data.csv') # saves results including links for the searched keyword
'''