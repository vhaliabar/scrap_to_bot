import requests
from bs4 import BeautifulSoup
import time


url = 'https://www.tesmanian.com/blogs/tesmanian-blog'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
articles = soup.find_all('blog-post-card', class_='blog-post-card snap-center group')
for article in articles:
    title = article.find('p', class_='h3').text
    link = article.find('a')['href']
    date = article.find('span', class_='text-sm').text
    info = [title, date, link]
    print(info)