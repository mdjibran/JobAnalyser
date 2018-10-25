#from urllib.request import urlopen
#from bs4 import BeautifulSoup
import os
import Methods as m

'''
#source = "https://ca.indeed.com/jobs?q="
#role = "big data developer&".replace(" ", "+")
#location = "Toronto ON&radius=100".replace(" ", "+")
#url = source + role + location
#print("URL : "+ url)
#openFiles()
#page = urlopen(url)
#soup = BeautifulSoup(page, "html.parser")
#print(soup.text)
'''

for word in m.initialFileRead():
    #if not checkIfAnalysed(word):
    if word.isalnum():
        os.system('cls')
        print(word)
        line = "\n" + word +","
        m.performAction(m.getUserInput(), line)