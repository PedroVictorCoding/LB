from libgen_api import LibgenSearch #For search
import os, sys, json
from run import bc 
import subprocess
import requests 
from bs4 import BeautifulSoup
from pathlib import Path


home = str(Path.home())

s = LibgenSearch()
filters = {
  	"Language"  : "English",
  }

def options():
    print("\n\nPick one of the following:\n1 - Search by Title\n2 - Search by Author\n3 - Help\n0 - Quit")
    given_option = input("Option: ")

    if given_option == "0":
        close()
    elif given_option == "1":
        search_for_title()
    elif given_option == "2":
        search_for_author()
    else:
        helper()


def close():
    os.system("deactivate")
    quit()


def helper():
    print("\n\nLibgen Search Tool with TOR Network \nSelect one option to search")
    options()


def search_for_title():
    given_title = input("\n\nEnter the title: ")

    results = s.search_title_filtered(given_title, filters)

    with open('bookinfo.json', 'w') as json_file:
        json.dump(results, json_file)

    f = open("bookinfo.json",) 
    
    # returns JSON object as  
    # a dictionary 
    bookdata = json.load(f) 
    j = 0
    while j < len(bookdata):
        bookinfo = bookdata[j]
        print(bc.OKGREEN + "Title: " + bc.ENDC + bookinfo['Title'])
        print(bc.OKGREEN + "Author: " + bc.ENDC + bookinfo['Author'])
        print(bc.OKGREEN + "ID: " + bc.ENDC + bookinfo['ID'])
        print(bc.OKGREEN + "Pages: " + bc.ENDC + bookinfo['Pages'] + bc.OKGREEN + "\tFormat: " + bc.ENDC + bookinfo['Extension'] + bc.OKGREEN + "\tPublisher: " + bc.ENDC + bookinfo['Publisher'] + bc.OKGREEN + "\tYear: " + bc.ENDC + bookinfo['Year'])
        print("\n")
        j += 1

    given_ID = input("Select by ID: ")

    i = 0
    while i < len(bookdata):
        bookinfo = bookdata[i]
        if bookinfo['ID'] == given_ID:
            print("Downloading: " + bookinfo['Mirror_1'])

            page = requests.get(bookinfo['Mirror_1'])
            bs = BeautifulSoup(page.content, features='lxml')
            test = subprocess.Popen(["wget","-P", home + "/Downloads/", bs.find('a').get('href'),], stdout=subprocess.PIPE)
            output = test.communicate()[0]
            print(output)
            print("Saved to: " + home + "/Downloads")
        i += 1    



def search_for_author():
    given_title = input("\n\nEnter the Author: ")

    results = s.search_author_filtered(given_title, filters)

    with open('bookinfo.json', 'w') as json_file:
        json.dump(results, json_file)

    f = open("bookinfo.json",) 
    
    # returns JSON object as  
    # a dictionary 
    bookdata = json.load(f) 
    j = 0
    while j < len(bookdata):
        bookinfo = bookdata[j]
        print(bc.OKGREEN + "Author: " + bc.ENDC + bookinfo['Author'])
        print(bc.OKGREEN + "Title: " + bc.ENDC + bookinfo['Title'])
        print(bc.OKGREEN + "ID: " + bc.ENDC + bookinfo['ID'])
        print(bc.OKGREEN + "Pages: " + bc.ENDC + bookinfo['Pages'] + bc.OKGREEN + "\tFormat: " + bc.ENDC + bookinfo['Extension'] + bc.OKGREEN + "\tPublisher: " + bc.ENDC + bookinfo['Publisher'] + bc.OKGREEN + "\tYear: " + bc.ENDC + bookinfo['Year'])
        print("\n")
        j += 1

    given_ID = input("Select by ID: ")

    i = 0
    while i < len(bookdata):
        bookinfo = bookdata[i]
        if bookinfo['ID'] == given_ID:
            print("Downloading: " + bookinfo['Mirror_1'])

            page = requests.get(bookinfo['Mirror_1'])
            bs = BeautifulSoup(page.content, features='lxml')
            test = subprocess.Popen(["wget","-P", home + "/Downloads/", bs.find('a').get('href'),], stdout=subprocess.PIPE)
            output = test.communicate()[0]
            print(output)
            print("Saved to: " + home + "/Downloads")
        i += 1    



if __name__ == "__main__":
    ## Checking current ip
    os.system("curl ifconfig.me")
    print(" - " + bc.OKGREEN + "TOR IP" + bc.ENDC)
    options()

