from bs4 import BeautifulSoup
import requests
import shutil

raise_by = 0
multiply_by = 250
loop_done = False

while not loop_done and raise_by <= 39:
    html_page = requests.get('https://howrare.is/solsnatchers/?page={}&ids=&sort_by=rank'.format(raise_by))
    soup = BeautifulSoup(html_page.content, 'html.parser')

    images = soup.findAll('img')

    title = []
    for _ in soup.findAll('h3'):
        a = _.get_text()
        title.append(a)

    number = 0
    for i in images:
        image = i.attrs['src']

        full_url = image
        r = requests.get(full_url, stream=True)
        if r.status_code == 200:
            with open("{}_{}.png".format(int(number+((raise_by*multiply_by)+1)), title[number]), 'wb') as f: 
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
            number += 1
    
    raise_by += 1
    loop_done = False
