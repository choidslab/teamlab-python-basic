import urllib.request
import re

BASE_URL = "http://web.eecs.umich.edu/~radev/coursera-slides/"

html = urllib.request.urlopen(BASE_URL)
html_contents = str(html.read().decode('utf-8'))

url_list = re.findall(r"nlp[0-9a-zA-Z\_\.]*\.pdf", html_contents)
for url in url_list:
    file_name = "".join(url)
    full_url = BASE_URL + file_name
    print(full_url)
    fname, header = urllib.request.urlretrieve(full_url, file_name)
    print("ENd Download")
