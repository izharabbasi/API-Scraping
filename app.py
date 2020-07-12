import requests
import json
import csv
from urllib.parse import urljoin

def write_to_csv(data):
  headers = ['id','name','size','price','rating','img', 'url','subB']
  with open('data.csv', 'w' , encoding='utf-8') as f:
    writer = csv.DictWriter(f,headers)
    writer.writeheader()
    writer.writerows(data)

scrape_products = []
def scraper(pageNum = 1):
  url = "https://www.walgreens.com/productsearch/v1/products/search"

  payload = {"p":pageNum,"s":24,"view":"allView","geoTargetEnabled":False,"abtest":["tier2","showNewCategories"],"deviceType":"desktop","id":["350006"],"requestType":"tier3","sort":"Top Sellers","couponStoreId":"15196"}
  headers = {
    'content-type': 'application/json',
    'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
  }

  response = requests.post(url, headers=headers, data = json.dumps(payload))

  data = response.json()
  try:
    products = data['products']


    for product_info in products:
      p_info = product_info['productInfo']
      p = {
        'id':p_info['prodId'],
        'name':p_info['productDisplayName'],
        'size':p_info['productSize'],
        'price':p_info['priceInfo']['regularPrice'],
        'rating':p_info['averageRating'],
        'img':p_info['imageUrl'],
        'url':urljoin(base='https://www.walgreens.com/',url = p_info['productURL']),
        'subB':p_info['subBrandName']
      }
      scrape_products.append(p)
    pageNum += 1
    scraper(pageNum=pageNum)
  except KeyError:
    return
scraper()
print(len(scrape_products))
write_to_csv(scrape_products)