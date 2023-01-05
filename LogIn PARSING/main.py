from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent" : "MacBook"}

work = Session()

page = 1
result_text = "abc"
text = []
author = []


work.get("https://quotes.toscrape.com/page/", headers=headers) #Go to site's title
response = work.get("http://quotes.toscrape.com/login", headers=headers) #Go to site's login form
soup = BeautifulSoup(response.text, "html.parser") #Check code HTML
token = soup.find("input").get("value") #Find token
data = {"csrf_token" : token, "username" : "name", "password" : "password"} #Make dictionary with token and login form

while len(result_text) != 0:
    result = work.get("https://quotes.toscrape.com/page/" +str(page), headers=headers, data=data,
                      allow_redirects=True)  # Take our data and go to login user site's title

    result_text = BeautifulSoup(result.text, "html.parser").find_all("span", class_="text")

    result_author = BeautifulSoup(result.text, "html.parser").find_all("small", class_="author")

    page += 1

    for txt in result_text:
        text.append(txt.text)

    for auth in result_author:
        author.append(auth.text)

def base():
    for a, b in zip(text, author):
         yield a, b

print(base)
















