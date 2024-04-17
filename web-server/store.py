import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    categories = r.json()
    names = list(map(lambda category: category['name'],categories))
    image = list(map(lambda category: category['image'],categories))

    print(image)