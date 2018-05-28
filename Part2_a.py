import requests
from bs4 import BeautifulSoup
import re
import random

def fetch(url):
    response = requests.get(url)
    response = requests.get(url, cookies={'over18': '1'})
    return response

url = 'https://www.ptt.cc/bbs/index.html'
resp = fetch(url)
readResult = resp.text

print(readResult)

print("--------------------------------")

soup = BeautifulSoup(readResult, "html.parser")

for tag in soup.find_all('a', attrs={'href': re.compile("/bbs/.+index.html$")}):
    # Look at the parts of a tag
    tagWanted = tag.get('href')
    print('URL:', tagWanted)
print("--------------------------------")

choice = input("Which Broad you like: ")

url_choice = 'https://www.ptt.cc/bbs/' + choice + '/index.html'
print(url_choice)
resp_choice = fetch(url_choice)
readBoardResult = resp_choice.text
soup = BeautifulSoup(readBoardResult, "html.parser")

print('看板名稱', choice)
boardPost = soup.find_all('div', "r-ent")

for post in boardPost:

    try:
        tag = post.find('div', 'title').find('a')
        titleurl = post.find('a').get('href', None)
        articleurl = 'https://www.ptt.cc'+ titleurl
        title = tag.getText()
        date = post.find('div', 'date').getText()
        author = post.find('div', 'author').getText()

        getContent = fetch(articleurl)
        conentText = getContent.text
        articles = BeautifulSoup(conentText, "lxml").select('#main-content')

        for word in articles:
            content = word.text

        # print("網址", titleurl)
        print("標題: ", title)
        print("日期: ", date)
        print("作者: ", author)
        print("內文: ", content)

    except AttributeError:
        print("No post")