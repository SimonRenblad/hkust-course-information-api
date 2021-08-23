import requests
from bs4 import BeautifulSoup
import re

page = requests.get("https://prog-crs.ust.hk/ugcourse")

soup = BeautifulSoup(page.content, 'html.parser')

for link in soup.find_all('a', href=re.compile('\/ugcourse\/\d{4}-\d{2}\/[A-Z]{4}')):
    
    link = "https://prog-crs.ust.hk"+link.get('href')
    print(link)

    subpage = requests.get(link)

    subsoup = BeautifulSoup(subpage.content, 'html.parser')
    
    for course in subsoup.find_all("li"):
        code = course.select_one(".crse-code").get_text()
        title = course.select_one(".crse-title").get_text()
        credits = course.select_one(".crse-unit").get_text()
        print(code)
        print(title)
        print(credits)
    break