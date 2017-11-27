"""

 newsapi.py
 By Leo N.
 An implementation of the News API.
 Requirements: Python 3+, Internet, News API Key.

"""

# Importing Python web modules
import random, json, urllib.parse, requests



# ------- Global Variables ----- #

NEWS = []
ARTICLES = []

EVENTS = []
TITLES = []
CITIES = ['Dijon', 'Indianapolis', 'Chicago', 'Phoenix', 'Philadelphia',
          'Boulder', 'CapeTown', 'Luanda', 'Paris', 'Lisbon',
          'Porto', 'SaoPaulo', 'Portland', 'Seattle']


# ------------ NEWS ------------ #


def NewsObjects():
    # Developer API key
    key = "f355c018b1474aef93c183aebcb3b845"
    # API Endpoint: Querying News
    api = 'https://newsapi.org/v2/top-headlines?sources=bbc-news,associated-press,abc-news,cbc-news,engadget,the-economist,the-guardian-au&apiKey=' + key
    data = requests.get(
        api,
        verify = True,
    ).json()

    size = len(data['articles'])

    for i in range(size):
        ARTICLES.insert(i, data['articles'][i])

    return ARTICLES



# --------- EVENTMATE ---------- #


def BuildObjects():

    # Developer API key
    key = "PU66GQF3VVQ5HODZNZFH"

    length = len(CITIES)

    # API Endpoint: Querying events in a random city
    api = "https://www.eventbriteapi.com/v3/events/search/?location.address="

    rand = random.randint(0, length)
    city = CITIES[rand]
    API = api + city

    data = requests.get(
        API,
        headers = { "Authorization": "Bearer " + key,},
        verify = True,).json()

    size = len(data['events'])

    for index in range(size):
        title = data['events'][index]['name']['text']
        singleEvent = data['events'][index]

        EVENTS.insert(index, singleEvent)

        if title not in TITLES:
            TITLES.insert(index, title)

    return EVENTS, TITLES, city



# ------------------------------- #

def main():
    news = NewsObjects()

# ------------------------------- #

if __name__ == '__main__':
    main()
