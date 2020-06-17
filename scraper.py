import requests
from bs4 import BeautifulSoup

page_url = 'https://sites.google.com/a/ict.gnu.ac.in/sitenews/home/2020---even-sem/all-news---even-sem-2020'
page = requests.get(page_url)

page_raw = BeautifulSoup(page.content, 'html.parser')

notifs = page_raw.find_all("div", class_="announcement")

for notif in notifs:
    main_elem = notif.find('h4')
    time_elem = notif.find('span', dir='ltr')
    print(main_elem.text.strip())
    print(time_elem.text.strip())
    print()