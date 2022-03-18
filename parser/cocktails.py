from urllib import response
import requests
from bs4 import BeautifulSoup
import time
from random import randrange
import json

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

    urls_count = len(urls_list)

    s = requests.Session()
    result_data = []

    for url in enumerate(urls_list):
        response = s.get(url=url[1], headers=headers)
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
        
        cocktail_ingredient_tables = soup.find('dl', class_='ingredients').find_all('a', class_='common-good-info')
        cocktail_ingredient_list = []
        for ingredient in cocktail_ingredient_tables:
            cocktail_ing = ingredient.get_text(' ')
            cocktail_ingredient_list.append(cocktail_ing) 
        

        cocktail_tools_tables = soup.find('dl', class_='tools').find_all('a', class_='common-good-info')
        cocktail_tools_list = []
        for tools in cocktail_tools_tables:
            cocktail_tool = tools.get_text(' ')
            cocktail_tools_list.append(cocktail_tool)
        
        cocktail_img = f"https://ru.inshaker.com{soup.find('div', class_='image-box desktop').find('img').get('src')}"
        
        result_data.append(
            {
                'original_url': url[1],
                'cocktail_title': cocktail_title,
                'cocktail_tags': cocktail_tags_list,
                'cocktail_recipe': cocktail_recipe_list,
                'cocktail_ingredient': cocktail_ingredient_list,
                'cocktail_tools': cocktail_tools_list,
                'cocktail_image': cocktail_img
            }
        )
        
        print(f'Обработал {url[0] + 1}/{urls_count}')

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)


def main():
    get_cocktails_urls(url='https://ru.inshaker.com/cocktails')
    get_data('cocktails_urls.txt')


if __name__ == '__main__':
    main()
