''' 
The story behind the script:
My VTU 8th sem results were due and I had recently procured a monitor 
to look more hard-core at work like the other devs. 
Leveraging both these facts, I wrote a script to keep polling the VTU website. 
The result:
1. The monitor had a terminal running with this script - looks cooler than a wallpaper
2. I could check if my results were out (or not)
'''
import urllib
import re
from bs4 import BeautifulSoup
from lxml import html
import datetime

while(1):
    usn = "001"
    url1 = "http://results.vtu.ac.in/results17/result_page.php?usn=1pe13cs"
    page = urllib.urlopen(url1+usn)
    soup = BeautifulSoup(page, "lxml")
    textOnly = soup.get_text()

    notOut = re.search("Invalid", textOnly)

    if notOut:
        print "Results not yet out...chill", datetime.datetime.now().time()
        time.sleep(60*5)  

    else:
        print "PANIC!!!!!----PANIC--------PANIC---------PANIC-----------PANIC-----------"
        break
