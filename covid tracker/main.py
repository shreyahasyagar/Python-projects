from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="D:\My Projects\covid tracker\coronaIcon.ico",
        timeout= 10
    )

def getData(url):
        r=requests.get(url)
        return r.text

if __name__ == "__main__":
    #notifyMe("Shreya","Let's stop the spread of Corona virus together")
    myHtmldata=getData("https://www.mohfw.gov.in/")

    #print(myHtmldata)
    soup=BeautifulSoup(myHtmldata,"html.parser")
    myDataStr=""
    #print(soup.prettify())
    for tr in soup.find_all("tbody")[0].find_all("tr"):
        myDataStr+=tr.get_text()
    myDataStr = myDataStr[1:]

    itemList =myDataStr.split("\n\n")

    states= ["Karnataka","Maharashtra","Tamil Nadu","Kerala","Telangana"]
    for item in itemList[0:22]:
    
        dataList=item.split('\n')
        if dataList[1] in states:
            print(dataList)
            nTitle="Cases of Covid-19"
            nText= f"{dataList[0]}: Ind:{dataList[2]}"
            notifyMe(nTitle,nText)