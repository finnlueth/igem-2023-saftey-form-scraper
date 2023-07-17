import csv
import imp
from multiprocessing.connection import wait
from lxml import html
import requests
from requests_html import HTMLSession

def getIDs():
    list = []
    with open("teams.csv", mode='r') as f:
        file = csv.reader(f)
        for x in file:
            list.append([x[0], x[1]])
        del list[0]
    return list

def getSite(id, name):
    session = HTMLSession()
    url = "https://responsibility.igem.org/safety-forms/project-safety?teamId=4497"# + str(id)
    page = session.get(url)
    # page.html.render(timeout=32)
    print("Success: " + url)

    # # sel = '/html/body'
    # for x in page.html.xpath(sel):
    #         print("--------")
    #         print(x.text)

    f = open("site.html", "w")
    f.write(page.html.html)
    f.close()

    # sel = '#about-your-project > div:nth-child(2) > div:nth-child(3)'
    # for x in page.html.find(sel):
    #     print("--------")
    #     print(x.text)

def main():
    result = getIDs()
    print(getSite(4497, "munich"))
    with open('iGEM-Teams.csv', 'w') as f:
        write = csv.writer(f)
        write.writerows(result)

if __name__=="__main__":
    main()
    print("Done!")
