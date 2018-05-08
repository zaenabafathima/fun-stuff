import sys
import webbrowser
from googlesearch import search


if len(sys.argv) >= 2:
	query = sys.argv[1]
else:
	print("No query provided!")
	exit(0)

hit_list = []
for result in search(query, tld="co.in", num=10, stop=1, pause=2):
	hit_list.append(result)
	print(result)
    
# Opening the top result in Chrome
url = hit_list[0] 
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'    # for MacOS
webbrowser.get(chrome_path).open(url)

