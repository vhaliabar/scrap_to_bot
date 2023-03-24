import requests
from bs4 import BeautifulSoup
import time

# set up persistent session for login
session = requests.Session()


# re-authenticate user if response.status
def auth_my_user():
    login_url = 'https://www.tesmanian.com/wp-login.php'
    login_data = {
    'customer[email]': 'chort44@ukr.net',
    'customer[password]': 'wmPj!@4DBS8mPNV',
    }
    return session.post(login_url, data=login_data)


# creating function that sends messages to TelegramBot
def send_to_telegram(message):
    
    apiToken = '5989043694:AAE6u6rPQUr6Fd3Ve8Qv4aQ8xKBoy_FOJkA'
    chatID = '784199315'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        #print(response.text)
    except Exception as e:
        print(e)


def main():
    # set up initial variables for previous title and link
    prev_title = ''
    prev_link = ''
    
    # scraping loop with 15-second interval
    while True:
        # send GET request and parse HTML response
        url = 'https://www.tesmanian.com/blogs/tesmanian-blog'
        response = session.get(url)
        if response.status_code != 200:
            auth_my_user()
        else:
            soup = BeautifulSoup(response.text, 'html.parser')

            # extract title and link of first article
            articles = soup.find_all('blog-post-card',
                                     class_='blog-post-card blog-post-card--featured snap-center group rounded bg-secondary')
            title = articles[0].find('p', class_='h2').text
            link = articles[0].find('a')['href']


            # compare with previous title and link
            if title != prev_title or link != prev_link:
                base_url = 'https://www.tesmanian.com'
                url = base_url+link
                send_to_telegram(f'New article:\n{title}\nLink:\n{url}')

                # update previous title and link
                prev_title = title
                prev_link = link

            # pause script for 15 seconds
            time.sleep(15)
        
if __name__ == '__main__':
    main()