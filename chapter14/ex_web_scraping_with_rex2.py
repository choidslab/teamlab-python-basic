import urllib.request
import re

url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html"

html = urllib.request.urlopen(url)
html_contents = str(html.read().decode('utf-8'))

url_list = re.findall(r"(http)(.+)(zip)", html_contents)
print(url_list)
for url in url_list:
    print("".join(url))
