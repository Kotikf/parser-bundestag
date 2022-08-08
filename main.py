import requests
from bs4 import BeautifulSoup
import json

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
    
data = []


with open("list_urls.txt", "r", encoding="utf-8") as file:
    
    lines = [line.strip() for line in file.readlines()]

    for link in lines: 
        r = requests.get(link)
        req = r.content
        soup = BeautifulSoup(req, "lxml")
        person = soup.find(class_="bt-biografie-name").find("h3").text
        person_name_company = person.strip().split(",")
        person_name = person_name_company[0].strip()
        person_company = person_name_company[1].strip()
        person_profession = soup.find("div", class_="bt-biografie-beruf").find('p').text
        person_social = soup.find("ul", class_="bt-linkliste").find_all("a", class_="bt-link-extern")
        
        person_social_links = []
        for links in person_social:
            person_social_links.append(f"{links.get('href')}")
        

        persons_info = {
                "person_name": person_name,
                "person_company": person_company,
                "person_profession": person_profession,
                "person_social": person_social_links
        }
            
        data.append(persons_info)
        
with open("persons.json", "a", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
