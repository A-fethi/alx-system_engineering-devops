#!/usr/bin/python3
"""Function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Returns the first 10 hot posts ."""
    headers = {'User-Agent': 'A-fethi/1.0'}
    r = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                     headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        for child in data['data']['children'][:10]:
            title = child['data']['title']
            print(title)
    else:
        print("None")
