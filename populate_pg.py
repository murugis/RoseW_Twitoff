'''Populate TwitOff with users'''
import requests

URL = 'https://rosew-twitoff.herokuapp.com/user'

​
USERNAMES = [
    'BarackObama','jeffbezos','cecewinans','nytimes',
    'YouTube','elonmusk'
]
​
def populate_twitoff(url, usernames):
'''POST to url for each name in usernames'''
    with requests.Session() as session:
        for username in usernames:
            print(username)
            r = session.post(url, data={'user_name': username})
​
if __name__ == '__main__':

populate_twitoff(URL, USERNAMES)
