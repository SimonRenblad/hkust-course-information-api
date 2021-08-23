import requests
from bs4 import BeautifulSoup
import re
import json
import pickle

page = requests.get("https://prog-crs.ust.hk/ugcourse")

soup = BeautifulSoup(page.content, 'html.parser')

courses = {}

for link in soup.find_all('a', href=re.compile('\/ugcourse\/\d{4}-\d{2}\/[A-Z]{4}')):
    
    link = "https://prog-crs.ust.hk"+link.get('href')
    print(link)

    subpage = requests.get(link)

    subsoup = BeautifulSoup(subpage.content, 'html.parser')
    
    for course in subsoup.find_all("li"):
        course_data = {}
        code = course.select_one(".crse-code").get_text().replace(" ", "")
        title = course.select_one(".crse-title").get_text()
        credits = course.select_one(".crse-unit").get_text()
        credits = re.search(r"\d-\d|\d", credits).group()
        #print(code)
        #print(title)
        #print(credits)


        prerequisites = []
        corequisites = []
        exclusions = []
        description = ""

        for header in course.select(".header"):
            data = header.find_next_sibling("div").get_text()
            header = header.get_text()
            l = re.findall(r"[A-Z]{4}\s\d{4}", data)
            l = [n.replace(" ", "") for n in l]
            if re.match(r"Pre.*", header):
                prerequisites = l
            elif re.match(r"Cor.*", header):
                corequisites = l
            elif re.match(r"Exc.*", header):
                exclusions = l
            elif re.match(r"Des.*", header):
                description = data

        #print(description)
        #print(prerequisites)
        #print(corequisites)
        #print(exclusions)
        course_data["code"] = code
        course_data["title"] = title
        course_data["credits"] = credits
        course_data["description"] = description
        course_data["prerequisites"] = prerequisites
        course_data["corequisites"] = corequisites
        course_data["exclusions"] = exclusions
        courses[code] = course_data

with open('courses.pickle', 'wb') as handle:
    pickle.dump(courses, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("done")