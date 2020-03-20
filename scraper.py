import os
from dotenv import load_dotenv, find_dotenv
from datetime import date
import urllib3

class Article():
    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description

    def __str__(self):
        return "Title: " + self.title + "\n\tLink: " + self.link

    def title():
        return self.title

    def link():
        return self.link
    
    def description():
        return self.description

def getWebsite():
    # Pull webpage
    http = urllib3.PoolManager()
    date_string = date.today().strftime("%Y/%m/%d")
    homepage = str(http.request('GET', "https://www.letsrun.com/archive/" + date_string).data)

    # Get news portion
    start_index = homepage.find('<div id="front_page">')
    end_index = homepage.find('<div class="tw-text-center tw-p-4">')
    site = homepage[start_index:end_index]

    return site

def extractLinks(site):
    links = []
    
    idx = 0
    end_index = len(site)

    while idx < end_index:
        # Structure: <a href="link">"title"</a>

        # length of "<a href=" is 8 chars
        if site[idx:idx + 8] == "<a href=":
            
            # Extract link by parsing the href value
            link = ""
            idx = idx + 9 # skips past <a href=" to put idx at first char of url
            while site[idx] != '"':
                link += site[idx]
                idx += 1

            idx += 2 # brings us to first char (non-") of title
            
            # Extract title by parsing the contents of the <a></a> tag
            title = ""
            while site[idx] != "<":
                title += site[idx]
                idx += 1

            if link != "" and title != "":
                links.append(Article(title, link, ""))
                
        else:
            idx += 1

    return(links)
	

extractLinks(getWebsite())