from lxml import html
from fake_useragent import UserAgent
import requests

ua = UserAgent()
headers = {'User-Agent': ua.chrome}

products = []

page = requests.get('http://www.adidas.com/us/men?grid=true&sz=120&start=0', headers=headers)
tree = html.fromstring(page.content)

entries = tree.xpath('//div[@class="product-tile"]/div[1]/@data-context')

def parse_entry(entry):
    fields = entry.split(';')
    product = {
        'id': fields[0].split(':')[1],
        'sku': fields[1].split(':')[1],
        'name': fields[2].split(':')[1],
        'model': fields[3].split(':')[1]
    }
    return product

products += [parse_entry(entry) for entry in entries]

print products