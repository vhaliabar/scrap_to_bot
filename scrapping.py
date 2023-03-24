import requests
from bs4 import BeautifulSoup
import time
import telebot

# set up persistent session for login
session = requests.Session()
login_url = 'https://www.tesmanian.com/wp-login.php'
login_data = {
    'customer[email]': 'chort44@ukr.net',
    'customer[password]': 'wmPj!@4DBS8mPNV',
}
session.post(login_url, data=login_data)


# creating function that sends messages to TelegramBot
def send_to_telegram(message):
    
    apiToken = '5989043694:AAE6u6rPQUr6Fd3Ve8Qv4aQ8xKBoy_FOJkA'
    chatID = '784199315'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
        

# set up initial variables for previous title and link
prev_title = ''
prev_link = ''


#taking control over the bot
#bot = telebot.TeleBot("5989043694:AAE6u6rPQUr6Fd3Ve8Qv4aQ8xKBoy_FOJkA", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


# scraping loop with 15-second interval
while True:
    # send GET request and parse HTML response
    url = 'https://www.tesmanian.com/blogs/tesmanian-blog'
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # extract title and link of first article
    articles = soup.find_all('blog-post-card', class_='blog-post-card snap-center group')
    #print(articles[0])
    title = articles[0].find('p', class_='h3').text
    link = articles[0].find('a')['href']


    # compare with previous title and link
    if title != prev_title or link != prev_link:
        # print('New article:', title)
        # print('Link:', link)
        base_url = 'https://www.tesmanian.com/'
        url = base_url+link
        send_to_telegram(f'New article:\n{title}')
        send_to_telegram(f'Link:\n{url}')

        # update previous title and link
        prev_title = title
        prev_link = link

    # pause script for 15 seconds
    time.sleep(15)