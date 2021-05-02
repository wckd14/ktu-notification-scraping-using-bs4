import requests
from bs4 import BeautifulSoup
import hashlib
import time

prevNote = ''

while True:
    URL = 'https://ktu.edu.in/home.htm'
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    
    results = soup.find_all("ul", class_="annuncement")
    #print(results[0].find_all("a"))
    #list of a tags a_tags
    a_tags = results[0].find_all("a")
    
    for i in range(5):
        temp = a_tags[i].find_all(text=True)
        print(temp[0])
    #print(results[0].find_all("a"))
    newNote = a_tags[i].find_all(text=True)[0]
    if prevNote == newNote:
        print("\n No Change Yet \n")
        pass
    else:
        print("\n !!New Notice Published!! \n")
        prevNote = newNote
    time.sleep(30)
        
