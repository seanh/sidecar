THEME = "."
AUTHOR = "Sean Hammond"
SITENAME = "Sidecar"
SITESUBTITLE = "Sidecar Demo"
SITEBIO = 'This is the demo site for <a href="https://github.com/seanh/sidecar">Sidecar</a>, a theme for the <a href="https://getpelican.com/">Pelican</a> static site generator. See the <a href="{SITEURL}/about/">about</a> page for more about Sidecar and its features.'
AVATAR_URL = "{SITEURL}/{THEME_STATIC_DIR}/images/avatar.jpg"
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
GITHUB_URL = "https://github.com/seanh/sidecar"
DEFAULT_CATEGORY = "Tech"
DEFAULT_DATE_FORMAT = "%B, %Y"
FORMATTED_FIELDS = ["summary", "subheading"]

FEED_DOMAIN = SITEURL

# Make the URLs of article permalink pages nicer.
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SOURCE_URL = "{article.url}index{OUTPUT_SOURCES_EXTENSION}"

# Make the URLs of period archive pages nicer.
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
YEAR_ARCHIVE_URL = "{date:%Y}/"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"
MONTH_ARCHIVE_URL = "{date:%Y}/{date:%m}/"
DAY_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/index.html"
DAY_ARCHIVE_URL = "{date:%Y}/{date:%m}/{date:%d}/"

# Make the URLs of static pages nicer.
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SOURCE_URL = "{page.url}index{OUTPUT_SOURCES_EXTENSION}"

SIDECAR_NAVBAR = [
    "HOME",
    "SPACE",
    "PAGES",
    "ARCHIVES",
]

SIDECAR_TAGLINE = [
    "TIME",
    "TAGS",
    "SOURCE",
]
