import pyshorteners

url = input("Enter the URL: ")

def shorturl(url):
       s = pyshorteners.Shortener()
       print(s.tinyurl.short(url))

shorturl(url)