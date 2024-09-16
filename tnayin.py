import requests
from bs4 import BeautifulSoup

link = 'https://browser-info.ru/'
response = requests.get(link).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find_all('div', id='tool_padding')

check_js = soup.find_all('div', id='javascript_check')
print(check_js)

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(response)