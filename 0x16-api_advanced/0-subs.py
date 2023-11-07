#!/usr/bin/python3
"""Function that queries the Reddit API and
returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subs, 0 if the given subreddit is invalid."""
    headers = {'User-Agent': 'A-fethi/1.0'}
    r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                     headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        subs = data['data']['subscribers']
        return subs
    return 0
