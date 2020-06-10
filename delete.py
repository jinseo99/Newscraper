import requests

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
headers = {'User-Agent': user_agent}

test_url = "http://thechart.blogs.cnn.com/2011/01/18/men-have-upper-hand-in-sexual-economy/"
req = requests.get(url=test_url, headers=headers, verify=False)


from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

article = ''

print('skipped \"Goose cannot extract article\"')
