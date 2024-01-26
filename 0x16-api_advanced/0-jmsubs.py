#!/usr/bin/python3
"""Get subreddit count by querying API"""

import requests


def number_of_subscribers(subreddit):
    """Request the number of subscribers in subreddit from the api"""
    user_agent = '0x16-kacchi'
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    headers = {'User-Agent': user_agent}

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return (0);

    data = r.json().get['data']
    # extract a list of the page
    pages = data['children']
    # extract data from first page
    page_data = pages[0]['data']
    # return number of subreddit subs
    return page_data['subreddit_subscribers']
