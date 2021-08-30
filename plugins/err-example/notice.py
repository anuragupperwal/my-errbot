import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.uietkuk.ac.in/')
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find( class_ ='wpb_text_column wpb_content_element')
    
result = []

def notice_fetcher():
    
    for i in reversed(content.find_all('a')):
        result.append({
            'title': i.get_text(),
            'link': i['href']
        })
    strr = ''
    for i in result:    
        tit=i['title']
        lin=i['link']
        strr = strr + '\nNotice: ' + tit + '\nLink: ' + lin + '\n' + '\n'
    return strr


def cse():
    for i in reversed(content.find_all('a')):
        result.append({
            'title': i.get_text(),
            'link': i['href']
        })
    strr = ''
    for i in result:
        tit=i['title']
        lin=i['link']
        splits = tit.split()
        for s in splits:
            if s== 'CSE':
                strr = strr + '\nNotice: ' + tit + '\nLink: ' + lin + '\n' + '\n'
    return strr

def ece():
    for i in reversed(content.find_all('a')):
        result.append({
            'title': i.get_text(),
            'link': i['href']
        })
    strr = ''
    for i in result:
        tit=i['title']
        lin=i['link']
        splits = tit.split()
        for s in splits:
            if s== 'ECE':
                strr = strr + '\nNotice: ' + tit + '\nLink: ' + lin + '\n' + '\n'
    return strr

def me():
    for i in reversed(content.find_all('a')):
        result.append({
            'title': i.get_text(),
            'link': i['href']
        })
    strr = ''
    for i in result:
        tit=i['title']
        lin=i['link']
        splits = tit.split()
        for s in splits:
            if s== 'ME':
                strr = strr + '\nNotice: ' + tit + '\nLink: ' + lin + '\n' + '\n'
    return strr

def bt():
    for i in reversed(content.find_all('a')):
        result.append({
            'title': i.get_text(),
            'link': i['href']
        })
    strr = ''
    for i in result:
        tit=i['title']
        lin=i['link']
        splits = tit.split()
        for s in splits:
            if s == 'BT':
                strr = strr + '\nNotice: ' + tit + '\nLink: ' + lin + '\n' + '\n'

    return strr
    