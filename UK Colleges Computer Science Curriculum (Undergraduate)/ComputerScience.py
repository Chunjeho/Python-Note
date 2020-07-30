import requests
from bs4 import BeautifulSoup

def UniTables():
    result = requests.get("https://www.theguardian.com/education/ng-interactive/2019/jun/07/university-guide-2020-league-table-for-computer-science-information")

    soup = BeautifulSoup(result.text, "html.parser")
    tables = soup.find("tbody")

    return tables

def UniInfo():

    tables = UniTables()
    uniNames = []
    uniNameRows = tables.find_all("tr", {"class":"c-table__row"})
    uniLinkRows = tables.find_all("tr", {"class":"c-table__row--course-list"})

    cs = []

    _curriculum = []

    for uniNameRow in uniNameRows:
        uniName = uniNameRow.find("td", {"class":"c-table__data--name"})

        if uniName is not None:
            uniName = uniName.find("a").get_text(strip = True)
            uniNames.append(uniName)

        else:
            continue

    for i in range(len(uniNames)):
        links = uniLinkRows[i].find_all("a", {"class":"c-course-list__course-link"})

        for link in links:
            cs.append({"University":uniNames[i], "Course":link.get_text(strip = True), "link":link["href"]})

        _curriculum.append(cs)
    
    return _curriculum