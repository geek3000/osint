# coding: utf-8
from bs4 import BeautifulSoup
import requests
from termcolor import colored

def on_telegram(username):
    url="https://t.me/"+username
    try:
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')

        for div in soup.find_all("div"):
            if div.get('class')==["tgme_page_title"]:
                
                return div.text
    except:
        print(colored("An error occured", "red"))

def on_twitter(username):
    url="https://twitter.com/"+username
    try:
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        
        for div in soup.find_all("div"):
            if div.get('class')==["errorpage-topbar"]:
                return None
        return True
    except:
        print(colored("An error occured", "red"))

def on_instagram(username):
    url="https://www.instagram.com/"+username
    try:
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        
        body=soup.find("body")
        if body.get('class')==[" p-error dialog-404"]:
                return None
        return True
    except:
        print(colored("An error occured", "red"))
        
print(colored("OSINT - Open Source Intelligence on Public Platform", "red"))

username=input(colored("Enter username:", "blue"))
name=on_telegram(username)
if(name):
    print(colored("On Telegram ", "green") + colored(name, "yellow"))
else:
    print(colored("Not found on Telegram", "red"))
rep=on_twitter(username)
if(rep):
    print(colored("On Twitter", "green"))
else:
    print(colored("Not found on Twiiter", "red"))
rep=on_instagram(username)
if(rep):
    print(colored("On instagram", "green"))
else:
    print(colored("Not found on instagram", "red"))

