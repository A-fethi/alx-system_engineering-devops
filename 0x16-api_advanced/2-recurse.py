#!/usr/bin/python3
"""Function that queries the Reddit API and
returns a list containing the titles of all
hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all
    hot articles for a given subreddit."""
    headers = {'User-Agent': 'A-fethi/1.0'}
    r = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                     headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        for child in data['data']['children']:
            title = child['data']['title']
            hot_list.append(title)
        return recurse(subreddit, hot_list)
    else:
        return None
