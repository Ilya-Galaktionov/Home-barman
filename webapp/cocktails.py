from urllib import response
import requests
from bs4 import BeautifulSoup
import time
from random import randrange

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
    for page in range(1, 2):
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

    for url in urls_list[:1]:
        response = s.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        cocktail_title = soup.find('div', class_='common-title header').find('h1', class_='common-name').text.strip()
        cocktail_tags = soup.find('ul', class_='tags').find_all('li', class_='item')
        for tg in cocktail_tags:
            cocktails_tags_list = []
            tg_c = tg.get_text().strip()
            cocktails_tags_list.append(tg_c)
        
        cocktail_recipe = soup.find('ul', class_='steps').find_all('li')
        cocktails_recipe_list = []
        for recipes in cocktail_recipe:
            cocktail_rcp = recipes.get_text().strip()
            cocktails_recipe_list.append(cocktail_rcp)   
        
        print(cocktails_recipe_list)


def main():
    # print(get_cocktails_urls(url='https://ru.inshaker.com/cocktails'))
    get_data('cocktails_urls.txt')


if __name__ == '__main__':
    main()
