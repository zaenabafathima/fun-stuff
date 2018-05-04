#something I've been wanting to do for a while...
import urllib
import re
# import requests
from bs4 import BeautifulSoup
from lxml import html
# import operator
# import time
import datetime

while(1):

    usn = "179"

    url1 = "http://results.vtu.ac.in/results17/result_page.php?usn=1pe13cs"
    page = urllib.urlopen(url1+usn)
    soup = BeautifulSoup(page, "lxml")
    textOnly = soup.get_text()

    notOut = re.search('Invalid', textOnly)

    if notOut:
        print "Results not yet out...chill", datetime.datetime.now().time()
        time.sleep(300)

    else:
        print "PANIC!!!!!----PANIC--------PANIC---------PANIC-----------PANIC-----------"
        break
