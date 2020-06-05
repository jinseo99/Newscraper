from newspaper import Article

article = Article("https://www.businessinsider.com/elon-musk-proved-tesla-doesnt-need-advertising-2020-5")
article.download()
article.parse()
article.nlp()

print(article.summary)