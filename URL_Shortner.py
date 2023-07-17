#Import pyshortner library to impliment for the url shorting
import pyshorteners

#Taking user input 
Userer_enterd_url = input('Please Enter The URL: ')
print('Here is your shorted URL:  ',end)

#Function take input and print shorted url
def url_Shortner(url):
    #Creating a variable of pyshortner library to use it for url shortening
    pshort = pyshorteners.Shortener()
    print(pshort.tinyurl.short(url))

#Calling url shortening function
url_Shortner(Userer_enterd_url)
