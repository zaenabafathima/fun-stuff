'''
A video featuring my 1st semester classroom went viral and I thought it would
be fun to see how the view count increases over time.
This script just checks the view count every 5 minutes and writes it into a file
(we'll generate a graph off it)
'''

import urllib.request
import re
from bs4 import BeautifulSoup
from lxml import html
import operator
import csv
import time
from datetime import datetime

while(1):
	url = "https://www.youtube.com/watch?xxxxxxxxxxxxxxx"
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, "lxml")
	textOnly = soup.get_text()

	# looking to pull out the views on the video now
	views = re.search(r'([0-9,]+) views', textOnly).group(1)
	temp = views.split(',')
	view_count = ''.join(temp)
	print("view count is", view_count)

	
	# I should eventually set up a cron job to do this repeatedly...but first! The file
	now = datetime.time(datetime.now())
	formatted_now = now.strftime('%H:%M')
	print("formatted now is", formatted_now)

	fhandle = open('video_stats6.txt', 'a')
	fhandle.write(formatted_now+'\t'+view_count+'\n')
	time.sleep(60*5)










