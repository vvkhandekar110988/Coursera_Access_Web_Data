# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

num = 0
lst1 = ['http://py4e-data.dr-chuck.net/known_by_Gytis.html']
print('Fikret')
while num < 7:
    url = lst1[0]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags[17:18]:
        tag1 = tag.get('href', None)
        print(tag.text)
        lst1[0] = tag1
    num += 1






