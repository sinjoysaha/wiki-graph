import requests
from bs4 import BeautifulSoup
import networkx as nx

WIKI_HOME_URL = 'https://en.wikipedia.org'


def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_href_list(soup):
    p_list = soup.find('div', attrs={'class': 'mw-parser-output'}).find_all('p', recursive=False)
#     print(p_list)
    href_list = []
    for p in p_list:
        a_tag_list = p.find_all('a', recursive=False)
        if a_tag_list:
            for a_tag in a_tag_list:
                href = a_tag.attrs['href']
                if 'Help' not in href:
                    href_list.append(href)  
            break

    return href_list
    
def get_word_from_href(href_list):
    next_word_list = []
    for href in href_list:
        word = href.split('/')[-1].split('#')[0]
        next_word_list.append(word)     

    return next_word_list

def get_next_word(SEARCH_WORD):
    next_word_list = get_word_from_href(href_list)
    
    
        
    