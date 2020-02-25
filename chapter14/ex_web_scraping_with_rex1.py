import urllib.request
import re

url = "http://goo.gl/U7mSQl"
html = urllib.request.urlopen(url)
html_contents = str(html.read())

id_result = re.findall(r"([a-zA-Z0-9]+\*)", html_contents)
print(type(id_result))
print(id_result)

for result in id_result:
    print(result)