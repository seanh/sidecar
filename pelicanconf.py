THEME = "."
AUTHOR = "Sean Hammond"
SITENAME = "Sidecar"
SITEURL = "http://localhost:8000"
PATH = "content"
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_SOURCES = True
TYPOGRIFY = True
TYPOGRIFY_DASHES = "oldschool"
TIMEZONE = "Europe/London"
DEFAULT_LANG = "en"
DEFAULT_PAGINATION = 10
CATEGORIES_SAVE_AS = "categories/index.html"
CATEGORIES_URL = "categories/"
TAGS_SAVE_AS = "tags/index.html"
TAGS_URL = "tags/"
AUTHORS_SAVE_AS = "authors/index.html"
AUTHORS_URL = "authors/"
ARCHIVES_SAVE_AS = "archives/index.html"
ARCHIVES_URL = "archives/"
DISPLAY_CATEGORIES_ON_MENU = True
GITHUB_URL = "https://github.com/seanh/sidecar"
DEFAULT_CATEGORY = "Tech"

FEED_DOMAIN = SITEURL

LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Oatcake", "https://github.com/seanh/oatcake"),
    ("GitHub", "https://github.com/seanh/sidecar"),
)

SOCIAL = [
    ("Mastodon", "https://mastodon.social/@seanh"),
    ("Pinboard", "https://pinboard.in/u:seanh"),
]

SIDECAR_MENU = [
    "HOME",
    "MENUITEMS",
    "PAGES",
    "TAGS",
    "AUTHORS",
    "ARCHIVES",
]

SIDECAR_TAGLINE = [
    "AUTHORS",
    "TIME",
    "TAGS",
]
