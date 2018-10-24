import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from past.builtins.misc import raw_input
import os


def openFiles():
    # Open all required files
    techSkills = open(r"techSkills.txt", "w+") # skill, company, url, job title
    softSkills = open(r"softSkills.txt", "w+") # skill, company, url, job title,
    text = open(r"text.txt", "w+")             # word, url
    processedUrls = open(r"processedUrls.txt", "w+") # url
    
source = "https://ca.indeed.com/jobs?q="
role = "big data developer&".replace(" ", "+")
location = "Toronto ON&radius=100".replace(" ", "+")

def insertTech(line):
    with open("techSkills.txt", "a") as dbFile:
        dbFile.write(line)
        dbFile.close()
    return "success"

def insertSoft(line):
    with open("softSkills.txt", "a") as dbFile:
        dbFile.write(line)
        
    return "success"

def insertText(line):
    with open("text.txt", "a") as dbFile:
        dbFile.write(line)
    return "success"

def insertUrl():
    with open("processedUrls.txt", "a") as dbFile:
        dbFile.write("appended text")
    return "success"    

def checkIfAnalysed(wrd):
    exists = False
    with open("techSkills.txt", "r") as dbFile:
        existing = dbFile.readlines()
        skills = []
        for line in existing:
            skills.append(line.split(',')[0])
        if wrd in skills:
            exists = True
    
    with open("softSkills.txt", "r") as dbFile:
        existing = dbFile.readlines()
        skills = []
        for line in existing:
            skills.append(line.split(',')[0])
        if wrd in skills:
            exists = True
    
    with open("text.txt", "r") as dbFile:
        existing = dbFile.readlines()
        skills = []
        for line in existing:
            skills.append(line.split(',')[0])
        if wrd in skills:
            exists = True
    return exists

def getUserInput():
    opt = raw_input("Options: \n 1 - Tech \n 2 - Soft \n 3 - Text \n Selection: ")
    return opt

def performCleanUp():
    analysedWords = []
    rawWords = []
    remainingWords = ''
    
    with open("techSkills.txt", "r") as dbFile:
        existing = dbFile.readlines()
        for line in existing:
            analysedWords.append(line.split(',')[0])
        
    with open("softSkills.txt", "r") as dbFile:
        existing = dbFile.readlines()
        for line in existing:
            analysedWords.append(line.split(',')[0])
        
    with open("text.txt", "r") as dbFile:
        existing = dbFile.readlines()
        for line in existing:
            analysedWords.append(line.split(',')[0])
            
    with open("posting.txt", "r") as dbFile:
        existing = dbFile.read()
        existing = re.sub(r'([^\s\w]|_)+', ' ', existing)
        for line in set(existing.split(' ')):
            if len(line) > 0:
                rawWords.append(line.replace('\n', ' ').replace('\t', ' '))
    
    rawWords = set(rawWords)
    
    for word in rawWords:
        if word not in analysedWords:
            remainingWords += str(word) + ' '
    remainingWords = remainingWords.strip()
    
    with open("posting.txt", "w+") as dbFile:
        dbFile.write(remainingWords)
    
def performAction(opt, line):
    if opt == '1':
        insertTech(line)
    elif opt == '2':
        insertSoft(line)
    elif opt == '3':
        insertText(line)

    else:
        performCleanUp()
        print("Exiting Application...")
        exit(1)

def getRemainingWordCount():
    rawWords = []
    with open("posting.txt", "r") as dbFile:
        existing = dbFile.read().replace('\n', ' ').replace('\t', ' ')
        existing = re.sub(r'([^\s\w]|_)+', ' ', existing)
        for line in existing.split(' '):
            if line.isalnum():
                rawWords.append(line.strip())
    rawWords = set(rawWords)
    return "Remaining Words : " + str(len(rawWords))
            
    
url = source + role + location
#print("URL : "+ url)
#openFiles()
#page = urlopen(url)
postingText = ''
with open('posting.txt', 'r') as posting:
    postingText = posting.read().replace('\n', ' ').replace('\t', ' ')
postingText = re.sub(r'([^\s\w]|_)+', ' ', postingText)
print(getRemainingWordCount())
#soup = BeautifulSoup(page, "html.parser")
#print(soup.text)

postingList = list(postingText.split(' '))
for word in postingList:

    #if not checkIfAnalysed(word):
    os.system('cls')
    print(word)
    line = "\n" + word
    performAction(getUserInput(), line)