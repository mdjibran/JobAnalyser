import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from past.builtins.misc import raw_input
import os

path = "db/"

def openFiles():
    # Open all required files
    techSkills = open(r"techSkills.txt", "w+") # skill, company, url, job title
    softSkills = open(r"softSkills.txt", "w+") # skill, company, url, job title,
    text = open(r"text.txt", "w+")             # word, url
    processedUrls = open(r"processedUrls.txt", "w+") # url
 
def insertTech(line):
    with open(path+"techSkills.txt", "a") as dbFile:
        dbFile.write(line)
        dbFile.close()
    return "success"

def insertSoft(line):
    with open(path+"softSkills.txt", "a") as dbFile:
        dbFile.write(line)
        
    return "success"

def insertText(line):
    with open(path+"text.txt", "a") as dbFile:
        dbFile.write(line)
    return "success"

def insertUrl():
    with open(path+"processedUrls.txt", "a") as dbFile:
        dbFile.write("appended text")
    return "success"    

def checkIfAnalysed(wrd):
    exists = False
    with open(path+"techSkills.txt", "r") as dbFile:
        existing = dbFile.readlines()
        skills = []
        for line in existing:
            skills.append(line.split(',')[0])
        if wrd in skills:
            exists = True
    
    with open(path+"softSkills.txt", "r") as dbFile:
        existing = dbFile.readlines()
        skills = []
        for line in existing:
            skills.append(line.split(',')[0])
        if wrd in skills:
            exists = True
    
    with open(path+"text.txt", "r") as dbFile:
        existing = dbFile.readlines()
        skills = []
        for line in existing:
            skills.append(line.split(',')[0])
        if wrd in skills:
            exists = True
    return exists

def getUserInput():
    opt = raw_input("Options: \n 1 - Tech \n 2 - Soft \n 3 - Text \n 0 - Perform Cleanup \n Selection: ")
    return opt

def performCleanUp():
    analysedWords = []
    rawWords = []
    remainingWords = ''
    
    with open(path+"techSkills.txt", "r") as dbFile:
        existing = dbFile.readlines()
        for line in existing:
            analysedWords.append(line.split(',')[0])

    with open(path+"softSkills.txt", "r") as dbFile:
        existing = dbFile.readlines()
        for line in existing:
            analysedWords.append(line.split(',')[0])
        
    with open(path+"text.txt", "r") as dbFile:
        existing = dbFile.readlines()
        for line in existing:
            analysedWords.append(line.split(',')[0])
            
    with open(path+"posting.txt", "r") as dbFile:
        existing = clearFormatting(dbFile.read())
        for line in set(existing.split(' ')):
            if line.isalnum():
                rawWords.append(line.replace('\n', ' ').replace('\t', ' '))
    
    rawWords = set(rawWords)
    
    for word in rawWords:
        if word not in analysedWords:
            remainingWords += str(word) + ' '
    remainingWords = remainingWords.strip()
    
    with open(path+"posting.txt", "w+") as dbFile:
        dbFile.write(remainingWords)
    print(getRemainingWordCount())
    input("Press ENTER key to continue..")
    
def performAction(opt, line):
    if opt == '1':
        insertTech(line)
    elif opt == '2':
        insertSoft(line)
    elif opt == '3':
        insertText(line)
    elif opt =='0':
        performCleanUp()
    else:
        performCleanUp()
        print("Exiting Application...")
        exit(1)

def getRemainingWordCount():
    rawWords = []
    with open(path+"posting.txt", "r") as dbFile:
        existing = clearFormatting(dbFile.read())
        
        for line in existing.split(' '):
            if line.isalnum():
                rawWords.append(line.strip())
    rawWords = set(rawWords)
    return "Remaining Words : " + str(len(rawWords))
            
def initialFileRead():
    postingText = ''
    with open(path+'posting.txt', 'r') as posting:
        postingText = clearFormatting(posting.read())
        
    postingList = list(postingText.split(' '))
    return postingList

def clearFormatting(txt):
    #txt = txt.replace('\n', ' ').replace('\t', ' ')
    #txt = re.sub(r'([^\s\w]|_)+', ' ', txt)
    return txt