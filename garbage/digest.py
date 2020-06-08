from urllib.parse import urlparse
import requests
from http.cookiejar import CookieJar
import lxml.html
import copy
import hashlib
import time 
import re

url = "https://www.businessinsider.com/elon-musk-proved-tesla-doesnt-need-advertising-2020-5"


parsed_url = urlparse(url)


cookies = CookieJar()
useragent = 'newspaper/0.2.8'
headers = {'User-Agent': useragent}
timeout = 7
response = requests.get(url=url, **{'headers': headers, 'cookies': cookies, 'timeout': timeout, 'allow_redirects': True})
html = response.text

doc = lxml.html.fromstring(html)
clean_doc = copy.deepcopy(doc)


raw_html = html.encode('utf-8', 'replace')
link_hash = '%s.%s' % (hashlib.md5(raw_html).hexdigest(), time.time())

title = ''

tag= 'title'
selector = 'descendant-or-self::%s' % (tag or '*')

elems = clean_doc.xpath(selector, namespaces=None)

txts = [i for i in elems[0].itertext()]
TABSSPACE = re.compile(r'[\s\t]+')
value = ' '.join(txts).strip()
value = re.sub(TABSSPACE, ' ', value)
value = ''.join(value.splitlines())

title_text = value.strip()
used_delimeter = False
title_text_h1 = ''

tag= 'h1'
selector = 'descendant-or-self::%s' % (tag or '*')
elems = clean_doc.xpath(selector, namespaces=None)
title_text_h1_list = []

for tag in elems:
    txts = [i for i in tag.itertext()]
    value = re.sub(re.compile(r'[\s\t]+'), ' ', ' '.join(txts).strip())
    value = ''.join(value.splitlines())
    title_text_h1_list.append(value.strip())

title_text_h1_list.sort(key=len, reverse=True)
title_text_h1 = title_text_h1_list[0]
title_text_h1 = ' '.join([x for x in title_text_h1.split() if x])


meta = doc.cssselect('meta[property="og:title"]')
content = meta[0].attrib.get('content', None)
title_text_fb = content.strip()


filter_regex = re.compile(r'[^\u4e00-\u9fa5a-zA-Z0-9\ ]')
filter_title_text = filter_regex.sub('', title_text).lower()
filter_title_text_h1 = filter_regex.sub('', title_text_h1).lower()
filter_title_text_fb = filter_regex.sub('', title_text_fb).lower()


title_text = title_text_h1
used_delimeter = True

#title = MOTLEY_REPLACEMENT.replaceAll(title_text)

title = title_text.replace("&#65533;", "")

filter_title = filter_regex.sub('', title).lower()
title = title_text_h1


#output_formatter = OutputFormatter(self.config)

