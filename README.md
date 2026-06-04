# Twitter Locality

Exploratory script/notebook for inferring a Twitter user's location from profile text, followers, friends, and related scraped pages.

## What is here

- `Tweeter_Stalk.py` - Python class with scraping, geocoding, and Tweepy-based helper methods.
- `Stalking_notebook.ipynb` - exploratory notebook using the same approach.

## Requirements

The original experiment used packages such as RoboBrowser, BeautifulSoup, GeoText, geopy, Tweepy, pandas, matplotlib, and pathos.

## Caveats

- Twitter/X APIs and web markup have changed since this was written.
- Authentication placeholders are intentionally blank in the script.
- Treat this as an archived research prototype unless the API layer and dependency versions are refreshed.
- Do not commit API keys or generated notebook checkpoints; configure credentials locally when modernizing the Tweepy layer.
