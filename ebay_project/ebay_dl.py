import argparse
from telnetlib import STATUS
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(prog = 'Ebay Scraper',description = 'donwload info from ebay and store on JSON',)
parser.add_argument('search_term')
parser.add_argument('--num_pages', default=10)
args = parser.parse_args()

print('args.search_terms =', args.search_term)

# have to download the first ten pages

items =[]

for page_number in range(1,int(args.num_pages)+ 1):
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='+args.search_term+'&_sacat=0&LH_TitleDesc=0&_pgn='+ str(page_number)
    print('url -', url)

# download html
    r = requests.get(url)
    status = r.status_code

    print('status =', status )
    html = r.text
 
#  Process html

    soup = BeautifulSoup(html, 'html.parser')
    
    item_names = soup.select(".s-item__title")
    for name in item_names:
        items.append({'name' : name.text})
    
    # This code is not working for me 
    free_returns = soup.select(".s-item__free-returns")
    for fr_status in free_returns:
        print('fr_status.text=', fr_status.text)



print('items=', len(items))


