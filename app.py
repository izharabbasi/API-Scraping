import requests
from fake_useragent import UserAgent
import json


ua = UserAgent()
url = "https://www.walgreens.com/productsearch/v1/products/search"
querystring = {'instart_disable_injection' : 'true'}
payload = {"p":3,"s":24,"view":"allView","geoTargetEnabled":False,"abtest":["tier2","showNewCategories"],"deviceType":"desktop","id":["350006"],"requestType":"tier3","sort":"Top Sellers","couponStoreId":"15196"}
headers = {
  'content-type': 'application/json',
  'User-agent': ua.random
  
}

response = requests.post(url, headers=headers, data = json.dumps(payload), params=querystring)

print(response.json())
