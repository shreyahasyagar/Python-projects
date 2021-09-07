from googlesearch import search
import webbrowser, time

query=input("Enter your query: ")

print("\n Some of the links are as follows: ")
for i in search(query,tld="com",num=10,stop=10,pause=2):
    
    print("Link: "+i)
    print("\n")

print("Opening your query in google search engine!\n")
time.sleep(2)

webbrowser.open("https://google.com/search?q="+ query)
    