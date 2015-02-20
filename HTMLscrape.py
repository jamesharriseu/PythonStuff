import requests
import sys
BeautifulSoup.path.append('Macintosh HD/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')
import BeautifulSoup

session = requests.session()

req = session.get('http://lxml.de/')

doc = BeautifulSoup.BeautifulSoup(req.content)

print doc.findAll('a', { "class" : "gp-share" })
