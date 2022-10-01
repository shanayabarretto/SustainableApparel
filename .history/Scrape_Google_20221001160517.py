# This file contains all methods relevant to getting the link results from a Google search.

from bs4 import BeautifulSoup
import requests
import lxml

def get_links(search_term, num_results=10, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", timeout=30, debug=False):
    """Returns a list of links from a Google search.
    Args:
        search_term (str): The search term to be used.
        num_results (int, optional): The number of results to be returned. Defaults to 10.
        user_agent (str, optional): The user agent to be used. Defaults to "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/
    """
    params = {'q': search_term, 'hl': 'en', 'gl': 'us', 'start': 0}
    headers = {'User-Agent': user_agent}
    items = []

    while num_results > 0:
        html = requests.get('https://google.com/search', params=params, headers=headers, timeout=timeout).text
        soup = BeautifulSoup(html, 'lxml')

        for result in soup.select('.tF2Cxc'):
            title = result.select_one('h3').text
            link = result.select_one('a').get('href')
            try: desc = result.select_one('.VwiC3b').text
            except: desc = None
        
        items.append((title, link, desc))
        num_results -= 1
        if debug: print(f"Found {title} - {link} - {desc}")
        
        if soup.select_one('.d6cvqb a[id=pnnext]'): params["start"] += 10
        else: break
    
    return items

print(get_links("Sustainability / eco-friendliness of Nike"))