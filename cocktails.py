from enum import unique
import requests
from bs4 import BeautifulSoup
import time
from random import randrange

from webapp.db import db
from webapp.cocktails.models import Cocktails, Tags, Recipe, Ingredients, Tools

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'
}


def get_cocktails_urls(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    pagination_count = int(59)

    cocktails_urls_list = []
    for page in range(pagination_count + 1):
        response = s.get(url=f'https://ru.inshaker.com/cocktails?random_page={page}', headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        cocktails_urls = soup.find_all('a', class_='cocktail-item-preview')

        for cu in cocktails_urls:
            c_url = cu.get('href')
            if c_url in cocktails_urls_list:
                continue
            else:
                cocktails_urls_list.append(c_url)

        time.sleep(randrange(2, 5))   
        print(f'Обработал {page}\{pagination_count}')

    with open('cocktails_urls.txt', 'w', encoding='utf-8') as file:
        for url in cocktails_urls_list:
            file.write(f'https://ru.inshaker.com{url}\n')

    return 'Работа по сбору ссылок выполнена'


def get_data(file_path):
    with open(file_path) as file:
        urls_list = [line.strip() for line in file.readlines()]

        s = requests.Session()

    for url in urls_list:
        response = s.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        cocktail_title = soup.find('div', class_='common-title header').find('h1', class_='common-name').text.strip()

        cocktail_tags = soup.find('ul', class_='tags').find_all('li', class_='item')
        cocktail_tags_list = []
        for tg in cocktail_tags:
            tg_c = tg.get_text().strip()
            cocktail_tags_list.append(tg_c)

        cocktail_recipe = soup.find('ul', class_='steps').find_all('li')
        cocktail_recipe_list = []
        for recipes in cocktail_recipe:
            cocktail_rcp = recipes.get_text().strip()
            cocktail_recipe_list.append(cocktail_rcp)

        cocktail_ingredient_tables = soup.find('dl', class_='ingredients').find_all('dd', class_='good')
        cocktail_ingredient_dict = []
        for tr in cocktail_ingredient_tables:
            cocktail_ingredient_dict.append({
                'name': tr.find('a', class_='common-good-info').contents[0],
                'amount': tr.find('amount').text,
                'unit': tr.find('unit').text,
            })

        cocktail_tools_tables = soup.find('dl', class_='tools').find_all('dd', class_='good')
        cocktail_tools_dict = []
        for tr in cocktail_tools_tables:
            cocktail_tools_dict.append({
                'name': tr.find('a', class_='common-good-info').contents[0],
                'amount': tr.find('amount').text,
                'unit': tr.find('unit').text,
            })

        cocktail_img = f"https://ru.inshaker.com{soup.find('div', class_='image-box desktop').find('img').get('src')}"

        save_cocktails(cocktail_title, cocktail_img)
        save_tags(cocktail_tags_list, cocktail_title)
        save_recipe(cocktail_recipe_list, cocktail_title)
        save_ingredient(cocktail_ingredient_dict,
                        cocktail_title)
        save_tools(cocktail_tools_dict, cocktail_title)


def save_cocktails(title, image):
    new_cocktail = Cocktails(title=title, image=image)
    db.session.add(new_cocktail)
    db.session.commit()


def save_tags(tags, title):
    my_cocktail = db.session.query(Cocktails).filter(Cocktails.title==title).first()
    for tag in tags:
        new_tag = Tags(tags=tag, cocktail_id=my_cocktail.id)
        db.session.add(new_tag)
        db.session.commit()


def save_recipe(my_recipe, title):
    my_cocktail = db.session.query(Cocktails).filter(Cocktails.title==title).first()
    for cocktail_recipe in my_recipe:
        new_tag = Recipe(recipe=cocktail_recipe, cocktail_id=my_cocktail.id)
        db.session.add(new_tag)
        db.session.commit()


def save_ingredient(my_ingredient, title):
    my_cocktail = db.session.query(Cocktails).filter(Cocktails.title==title).first()
    for cocktail_ingredient in my_ingredient:
        new_name = Ingredients(ingredient=cocktail_ingredient.get('name'),
                               amount=cocktail_ingredient.get('amount'),
                               unit=cocktail_ingredient.get('unit'),
                               cocktail_id=my_cocktail.id)
        db.session.add(new_name)
        db.session.commit()


def save_tools(tools, title):
    my_cocktail = db.session.query(Cocktails).filter(Cocktails.title==title).first()
    for tool in tools:
        new_tool = Tools(tool=tool.get('name'),
                         amount=tool.get('amount'),
                         unit=tool.get('unit'),
                         cocktail_id=my_cocktail.id)
        db.session.add(new_tool)
        db.session.commit()


def main():
    # get_cocktails_urls(url='https://ru.inshaker.com/cocktails')
    get_data('cocktails_urls.txt')
    

if __name__ == '__main__':
    main()
