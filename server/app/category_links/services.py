import requests

from bs4 import BeautifulSoup
from lxml import html
import lxml.etree

import sys
import category_links.models as models

headers = {
  'shop_id_1': {
    'SecFetchMode': 'navigate',
    'SecFetchUser': '?1',
    'UpgradeInsecureRequests': '1',
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Cookie': '_ga=GA1.2.1252715063.1557651982; _gcl_au=1.1.341974471.1560186450; _fbp=fb.1.1560186450299.249524527; _userGUID=0:jwqmqa3a:gs0YdxLsaVCNYQNRPiw47TFrb6GmmMh4; t_s_c_f_l=3HXCvb1tDHc%3D; sc=97FDAB98-F768-AAA2-9AAA-91637ADBE5B3; _gaexp=GAX1.2.D8pke4W_QjqyWvK_ZrBHuA.18073.1!QXFppiaISTqUIQ9HBKfeJQ.18144.0; city_id=13; _gcl_aw=GCL.1561276781.CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE; __utmz=45757819.1561276783.15.6.utmgclid=CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE|utmccn=(not%20set)|utmcmd=(not%20set); _gac_UA-5981690-1=1.1560280888.CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE; _gac_UA-63509214-3=1.1561276783.CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE; _gac_UA-5981690-6=1.1561276783.CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE; _gac_UA-63509214-1=1.1561277026.CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE; frontend=523c1168794249428ea42c43795467fd; _gid=GA1.2.1927733634.1566051168; store=default_ua; protocol=https; _hjid=4c1eceb4-37c3-4422-80fa-66569d5db0e3; detect_mobile_type=0; is_bot=0; __utmc=45757819; dSesn=1f6d663d-7556-8c5a-cfe9-c603abce16bb; _dvs=0:jzh9ampd:sawQ8h8yUepEAYDXYkBxGIZtoY6aeFgL; __utma=45757819.1252715063.1557651982.1566126580.1566150038.18; __utmt=1; __utmb=45757819.8.9.1566150063447; fp=60; lfp=8/17/2019, 5:12:48 PM; pa=1566150352017.99930.7900929866428965allo.ua0.13362229975648043+1'
  },
  'shop_id_2': {
    'SecFetchMode': 'navigate',
    'SecFetchUser': '?1',
    'UpgradeInsecureRequests': '1',
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Cookie': '_ga=GA1.2.1252715063.1557651982; _gcl_au=1.1.341974471.1560186450; _fbp=fb.1.1560186450299.249524527; _userGUID=0:jwqmqa3a:gs0YdxLsaVCNYQNRPiw47TFrb6GmmMh4; t_s_c_f_l=3HXCvb1tDHc%3D; sc=97FDAB98-F768-AAA2-9AAA-91637ADBE5B3; _gaexp=GAX1.2.D8pke4W_QjqyWvK_ZrBHuA.18073.1!QXFppiaISTqUIQ9HBKfeJQ.18144.0; city_id=13; _gcl_aw=GCL.1561276781.CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE; __utmz=45757819.1561276783.15.6.utmgclid=CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE|utmccn=(not%20set)|utmcmd=(not%20set); _gac_UA-5981690-1=1.1560280888.CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE; _gac_UA-63509214-3=1.1561276783.CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE; _gac_UA-5981690-6=1.1561276783.CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE; _gac_UA-63509214-1=1.1561277026.CjwKCAjwxrzoBRBBEiwAbtX1n9hLZa0Gohd6CSghEyAdIUyiskYO_i6UfXDRASCNmWQ-WWm4Z18KARoCk6AQAvD_BwE; frontend=523c1168794249428ea42c43795467fd; _gid=GA1.2.1927733634.1566051168; store=default_ua; protocol=https; _hjid=4c1eceb4-37c3-4422-80fa-66569d5db0e3; detect_mobile_type=0; is_bot=0; __utmc=45757819; dSesn=1f6d663d-7556-8c5a-cfe9-c603abce16bb; __utma=45757819.1252715063.1557651982.1566126580.1566150038.18; _dc_gtm_UA-63509214-3=1; fp=62; lfp=8/17/2019, 5:12:48 PM; pa=1566155125487.7780.9702081910563758allo.ua0.5097355530935455+1'
  }
}

class CategoryParser:
  def __init__(self):
    self.root = []
    self.category = {}

  def get_html(self, url):
    response = requests.get(url, headers=headers['shop_id_2'])
    return response.text

  def get_category(self, url):
    html = self.get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    menu = soup.find(id='menu')
    nav = menu.find('ul', class_='lvl1')
    list_category = { 'nav': nav }
    self.deep_parser(list_category)

  def deep_parser(self, list_category):
    collection = list_category['nav'].findChild(recursive=False)
    deep_collection = collection.find_all('a', class_='menu-item-lvl3')
    print(deep_collection)
    # for item in deep_collection:
    #   category = CategoryLinks(url=item.get('href'), category_value=item.getText(), shop_id="2")
    #   category.save()

  def setUp(self):
    self.get_category('https://www.moyo.ua/')

if __name__ == '__main__':
  # print(sys.path)
  CategoryParser().setUp()