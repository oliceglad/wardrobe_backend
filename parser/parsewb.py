import requests

man_clothes = {
    'man_clothes_cat': {
        'trousers': {
            'cat': '8144',
            'tag': 'men_clothes1'
        },
        'jacket': {
            'cat': '63011',
            'tag': 'men_clothes1'
        }
    }
}

woman_clothes = {
    'woman_clothes_cat': {

    }
}

class ParseWB:
    @staticmethod
    def get_category(category: str):
        url = f'https://catalog.wb.ru/catalog/{man_clothes["man_clothes_cat"][category]["tag"]}/catalog?appType=1&cat={man_clothes["man_clothes_cat"][category]["cat"]}&curr=rub&dest=-1257786&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,22,1,31,66,110,48,71,114&sort=popular&spp=0'
        response = requests.get(url=url)
        return response.json()