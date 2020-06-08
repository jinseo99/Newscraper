from newspaper import Article
import re
test_url = "https://www.businessinsider.com/elon-musk-proved-tesla-doesnt-need-advertising-2020-5"
test_url = "https://www.google.com/search?q=tesla&lr=lang_en&tbs=lr:lang_1en,cdr:1,cd_min:08/10/2015,cd_max:08/10/2015&tbm=nws&start=0"

#article = Article(test_url)
text = "a~"
print(re.search('\W',text))
"""
article.parse()
article.nlp()

print(article.summary)
"""
