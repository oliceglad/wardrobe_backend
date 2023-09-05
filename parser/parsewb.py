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
    def get_category(category, gender = 'man', count = 50):
        if gender == 'woman':
            url = f'https://catalog.wb.ru/catalog/{category}/catalog?appType=1&cat={woman["cat"][category]}&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,22,110,48,71,114&sort=popular&spp=0'
        else:
            url = f'https://catalog.wb.ru/catalog/{man["man_clothes_cat"][category]["tag"]}/catalog?appType=1&cat={man["man_clothes_cat"][category]["cat"]}&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,22,1,31,66,110,48,71,114&sort=popular&spp=0'
        response = requests.get(url = url)

        return ParseWB.prepare_items(response.json(), count)

    @staticmethod
    def prepare_items(response_dict, countGoods):

        countGoods = int(countGoods)
        products_list = []
        i = 0
        for product in response_dict['data']['products']:
            id_for_photo = str(product["id"])
            if i == countGoods:
                break
            products_list.append(
                {
                    'id':product['id'],
                    'name': check_name(product['name']),
                    'brand': product['brand'],
                    'price': product['salePriceU'] // 100,
                    'url': f'https://www.wildberries.ru/catalog/{product["id"]}/detail.aspx',
                    'images': [f'https://basket-10.wb.ru/vol{id_for_photo[:4]}/part{id_for_photo[:6]}/{id_for_photo}/images/c516x688/1.webp',
                               f'https://basket-05.wb.ru/vol{id_for_photo[:3]}/part{id_for_photo[:5]}/{id_for_photo}/images/c516x688/3.webp']
                }
            )
            i += 1


        return products_list