'''
After getting a panic alert from the previous script, this one will take the next step.
It fetches everyone's marks and prints them in descending order
A quick way to see who got more than me :P
'''
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


    url1 = "http://results.vtu.ac.in/reval_results17/result_page.php?usn=1pe13cs"
    page = urllib.urlopen(url1+usn)
    soup = BeautifulSoup(page, "lxml")
    textOnly = soup.get_text()

    name = re.search('(Student Name.[: \n\t\r]*)([A-Z \.]*)', textOnly)


    if name:
        marks = re.search('(Total Marks[\n]:[ ])([0-9]+)', textOnly)
        if marks:
            if name.group(2):
                phoneBook[name.group(2)] = int(marks.group(2))
        else:
            print "Can't find marks"
    else:
        print "I don't exist"

sorted_phoneBook = sorted(phoneBook.items(), key=operator.itemgetter(1))

for k in reversed(sorted_phoneBook):
    print k, (k[1]/750.0)*100
