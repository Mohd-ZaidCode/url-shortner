import pyshorteners

Userer_enterd_url = input('Please Enter The URL: ')

def url_Shortner(url):
    pshort = pyshorteners.Shortener()
    print(pshort.tinyurl.short(url))


url_Shortner(Userer_enterd_url)