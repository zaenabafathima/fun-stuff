# going to stalk UChicago Graduate Math Department... because I couldn't find better data

import urllib.request
import re
from bs4 import BeautifulSoup
from lxml import html
import operator
import csv
import time
from datetime import datetime



""" Welcome to my train of (bored) thoughts! We start off by fetching the webpage from the UChicago website.
I'm going to be needlessly detailed in documenting so bear with me
For that wel'll need to:
1. Store the URL
2. get the page using urllib
3. convert it to text only so we can actually do something with it
"""

while(1):

	url = "http://math.uchicago.edu/people/grad-students/"
	url = "https://www.youtube.com/watch?v=gdGmYDz_d6A&feature=share"
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, "lxml")
	textOnly = soup.get_text()

	# looking to pull out the views on the video now

	views = re.search(r'([0-9,]+) views', textOnly).group(1)
	temp = views.split(',')
	view_count = ''.join(temp)
	print("view count is", view_count)
	# print("Views match object is", views)

	"""
	I shall now setup a timer or cron to do this repeatedly...but first! The file
	"""

	now = datetime.time(datetime.now())
	formatted_now = now.strftime('%H:%M')
	print("formatted now is", formatted_now)

	fhandle = open('video_stats6.txt', 'a')
	fhandle.write(formatted_now+'\t'+view_count+'\n')
	time.sleep(60*5)










