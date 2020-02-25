import urllib.request

url = "http://storage.googleapis.com/patents/grant_full_text/2014/ipg140107.zip"

print("Start Download")

fname, header = urllib.request.urlretrieve(url, 'ipg140107.zip')

print("End Download")
