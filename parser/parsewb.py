import requests
from data import DataGender

man = DataGender.man_clothes
woman = DataGender.woman_clothes

def check_name(name):
    name_list = name.split()
    new_name = ''
    i = 0
    for name in name_list:
        if i == 2:
            break
        new_name += name + ' '
        i += 1
    return new_name

class ParseWB:
    @staticmethod
    def get_category(category):
        url = f'https://catalog.wb.ru/catalog/{man["man_clothes_cat"][category]["tag"]}/catalog?appType=1&cat={man_clothes["man_clothes_cat"][category]["cat"]}&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,22,1,31,66,110,48,71,114&sort=popular&spp=0'
        response = requests.get(url=url)

        return ParseWB.prepare_items(response.json())

    @staticmethod
    def prepare_items(response_dict):

        products_list = []
        i = 0
        for product in response_dict['data']['products']:
            if i == 10:
                break
            products_list.append(
                {
                    'id':product['id'],
                    'name': check_name(product['name']),
                    'brand': product['brand'],
                    'price': product['salePriceU'] // 100,
                    'url': f'https://www.wildberries.ru/catalog/{product["id"]}/detail.aspx'
                }
            )
            i += 1


        return products_list