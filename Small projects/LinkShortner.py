import pyshorteners
link=input("enter the link: ")
shortner = pyshorteners.Shortener()
x=shortner.tinyurl.short(link)
print("\nHere's your short link: \n",x)