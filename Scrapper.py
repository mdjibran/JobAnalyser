import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

def openFiles():
    # Open all required files
    techSkills = open(r"techSkills.txt", "w+") # skill, company, url, job title
    softSkills = open(r"softSkills.txt", "w+") # skill, company, url, job title,
    text = open(r"text.txt", "w+")             # word, url
    posting = open(r"posting.txt", "w+")       # 
    processedUrls = open(r"posting.txt", "w+") # url
    
source = "https://ca.indeed.com/jobs?q="
role = "big data developer&".replace(" ", "+")
location = "Toronto ON&radius=100".replace(" ", "+")

url = source + role + location
print("URL : "+ url)
openFiles()
#page = urlopen(url)
postingText = 'Big Data Developer Compunnel Software Group - Brampton, ON Job Summary I have a very urgent Direct Client requirement for Big Data Developer in Brampton ON. Please Let Me Know If you are comfortable for the below Job Description. Job Details: Role: - Big Data Developer Location: - Brampton ON Duration: - Full Time Responsibilities and Duties Job Description: At least Total 4+ years practical IT experience with Big Data systems, ETL, data processing, and analytics tools. Distributed computing experience using tools such as Hadoop and Spark. Proficiency in using query languages such as SQL, Hive and SparkSQL. Experience with entity-relationship modeling and understanding of normalization. Familiar with the concepts of dimensional modeling. Experience with Scala, Spark or Python. Able to understand various data structures and common methods in data transformation. Keeps up-to-date with newest technology trends. Job Type: Full-time Experience: practical IT: 7 years (Required)'
postingText = re.sub(r'([^\s\w]|_)+', '', postingText)
#soup = BeautifulSoup(page, "html.parser")
#print(soup.text)

postingList = list(list(postingText.split(' ')))
for word in postingList:
    if len(word) > 0:
        print(word)