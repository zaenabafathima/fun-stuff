#something I've been wanting to do for a while...
import urllib
import re
import requests
from bs4 import BeautifulSoup
from lxml import html
import operator
import csv

usn = ""
phoneBook = {}

for slno in range(1,186+1):
    if slno < 10:
        usn = "00" + str(slno)
    elif slno >= 10 and slno < 100:
        usn = "0"+str(slno)
    else:
        usn = str(slno)
    # print usn


    url1 = "http://results.vtu.ac.in/reval_results17/result_page.php?usn=1pe13cs"
    url2 = "http://results.vtu.ac.in/results/result_page.php?usn=1pe14cs"
    page=urllib.urlopen(url1+usn)
    soup=BeautifulSoup(page, "lxml")
    textOnly=soup.get_text()
    # print textOnly


    name = re.search('(Student Name.[: \n\t\r]*)([A-Z \.]*)', textOnly)


    if name:
        # print "Name:", name.group(2), "1PE13CS"+usn
        marks=re.search('(Total Marks[\n]:[ ])([0-9]+)', textOnly)
        if marks:
            if name.group(2):
                phoneBook[name.group(2)] = int(marks.group(2))
		#phoneBook[name.group(2)] = usn
                # print "Marks:", marks.group(2)
        else:
            print "Can't find marks"
    else:
        print "I don't exist"

sorted_phoneBook = sorted(phoneBook.items(), key=operator.itemgetter(1))

# with open('marksOfAll.csv', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(sorted_phoneBook)

for k in reversed(sorted_phoneBook):
    print k, (k[1]/750.0)*100
