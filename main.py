import requests
from bs4 import BeautifulSoup

# links_list = []
# for i in range(0, 740,20): #740
#     url = f"https://www.bundestag.de/ajax/filterlist/de/abgeordnete/biografien/862712-862712?limit=20&noFilterSet=true&offset={i}"
#     request = requests.get(url=url)
    
#     soup = BeautifulSoup(request.text, "lxml")
#     person_links = soup.find_all("a")
#     for link in person_links:
#         person_link = link.get("href")
#         links_list.append(person_link)

# with open("list_urls.txt", "a") as file:
#     for i in links_list:
#         file.write(f"https://www.bundestag.de{i}\n")
        

with open("list_urls.txt", "r") as file:
    

    lines = [line.strip() for line in file.readlines()]

    # for link in lines:
    #     r = requests.get(link)
    #     req = r.content
    #     soup = BeautifulSoup(req, "lxml")
    #     person = soup.find(class_="bt-biografie-name").find("h3").text
    #     person_name_company = person.strip().split(",")
    #     person_name = person_name_company[0]
    #     person_company = person_name_company[1]
    #     print(person_company.text)
    #     print(person_name.text)

    for link in lines:
        r = requests.get("https://www.bundestag.de/abgeordnete/biografien/A/abdi_sanae-861028")
        req = r.content
        soup = BeautifulSoup(req, "lxml")
        person = soup.find(class_="bt-biografie-name").find("h3").text
        person_name_company = person.strip().split(",")
        person_name = person_name_company[0]
        person_company = person_name_company[1]
        print(person_company)
        print(person_name)