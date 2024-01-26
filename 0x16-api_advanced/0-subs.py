#!/usr/bin/python3
"""Query Reddit API to determine subreddit count"""

import requests


def number_of_subscribers(subreddit):
    """same as above"""
    url = f"https://www.reddit.com/r/{subreddit}.json"
    headers = {"User-Agent": "0x16-api_advanced-the_kacchi"}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
            else:
                print("Invalid subreddit. Data format unexpected.")
                return 0
        elif response.status_code == 404:
            print("Subreddit not found.")
            return 0
        else:
            print(f"Error: {response.status_code}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
    except ValueError as e:
        print(f"Error: Unable to parse JSON response. {e}")
        return 0
