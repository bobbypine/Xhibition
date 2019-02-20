import requests
from bs4 import BeautifulSoup


def keysearch(key):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

    url = 'https://www.xhibition.co/sitemap_products_1.xml?from=4615990276&to=1633619705928'

    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')

    mylist = []
    global mylists
    mylists = mylist
    for items in soup.find_all("url"):
        item = items.find("image:title")
        if item is not None:
            title = item.text
            url = items.find("loc").text
            time = items.find("lastmod").text
            if keyword.lower() in title.lower():
                print(title, url, time)
                mylist.append(title)
            else:
                if keyword.lower() in url.lower():
                    mylist.append(url)
                    print('Keyword Not in Item Name, but Found {}'.format(url))
        if item is None:
            url2 = items.find("loc").text
            if keyword.lower() in url2.lower():
                    mylist.append(url2)
                    print('Keyword Not in Item Name, but Found {}'.format(url2))


while True:
    keyword = input('Enter Keyword, Hit Enter When Ready:').lower()
    if keyword == "":
        print('Program Ended')
        break
    keysearch(keyword)
    print()
    if len(mylists) == 0:
        print('No Results for {}'.format(keyword).title())
        print()
