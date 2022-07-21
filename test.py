from bs4 import BeautifulSoup
import requests

url = 'https://www.totalwine.com/wine/c/c0020?viewall=true&pageSize=120&userPrice=0-35userRating=80-100&sort=expert-ratings&aty=1,0,0,0&instock=1'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

page = requests.get(url, headers=headers)
html = page.content
soup = BeautifulSoup(html, 'html.parser')


def get_links():
    """
        The get_links accesses the URL provided and gets the available 
        links on just the first page.

        This method will eventually scrape all the available wines from
        the filtered list after I can automate moving to each page to 
        get the full list of wines from each page

        This method works by finding each h2 and getting the href link
        through the 'a' attribute.
    """
    wine_links = []
    h2_list = soup.find_all('h2')

    for h2 in h2_list:
        wine_links.append(h2.a['href'])

    return wine_links


def get_names():
    """
        The get_names function *WILL* retrieve a list of names from the
        filtered list of wines provided from the URL variable. 

        ***WORK IN PROGRESS***
    """
    h2_list = soup.find_all('h2')
    for h2 in h2_list:
        href_and_name = []
        href_and_name.append(h2.a)
        print(h2.a)


"""
def trying_to_get_regex_to_work():

    # Trying to use regex to filter out the names from h2_list

    links = soup.find_all('h2')

    regex = re.compile('<a href.*</a>')
    filtered = list(filter(regex.match, links))

    for id in filtered:
        print(id)
"""

