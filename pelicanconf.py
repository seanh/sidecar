THEME = "."
AUTHOR = "Sean Hammond"
SITENAME = "Sidecar"
SITESUBTITLE = "Sidecar Demo"
SITEBIO = """This is the demo site for <a href="https://github.com/seanh/sidecar">Sidecar</a>, a plain but pretty <a href="https://getpelican.com/">Pelican</a> theme based on <a href="https://www.seanh.cc/oatcake/">Oatcake</a>. See the <a href="{SITEURL}/about/">about</a> page for a tour."""
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
GITHUB_URL = "https://github.com/seanh/sidecar"
DEFAULT_DATE_FORMAT = "%-d %B, %Y"
FORMATTED_FIELDS = ["summary", "subheading", "subtitle"]

FEED_DOMAIN = SITEURL

# Make the URLs of article pages nicer.
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SOURCE_URL = "{article.url}index{OUTPUT_SOURCES_EXTENSION}"

# Make the URL of the archives page nicer.
ARCHIVES_SAVE_AS = "archives/index.html"
ARCHIVES_URL = "archives/"

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

# Make the URL of the authors page nicer.
AUTHORS_SAVE_AS = "authors/index.html"
AUTHORS_URL = "authors/"

# Make the URLs of author pages nicer.
AUTHOR_SAVE_AS = "author/{slug}/index.html"
AUTHOR_URL = "author/{slug}/"

# Make the URL of the tags page nicer.
TAGS_SAVE_AS = "tags/index.html"
TAGS_URL = "tags/"

# Make the URLs of tag pages nicer.
TAG_SAVE_AS = "tag/{slug}/index.html"
TAG_URL = "tag/{slug}/"

# Make the URL of the categories page nicer.
CATEGORIES_SAVE_AS = "categories/index.html"
CATEGORIES_URL = "categories/"

# Make the URLs of category pages nicer.
CATEGORY_SAVE_AS = "category/{slug}/index.html"
CATEGORY_URL = "category/{slug}/"

# Make pagination URLs nicer.
PAGINATION_PATTERNS = (
    (1, "{base_name}", "{save_as}"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)

SIDECAR_NAVBAR = [
    "HOME",
    "SPACE",
    "PAGES",
    "ARCHIVES",
]

SIDECAR_TAGLINE = [
    "AUTHORS",
    "TIME",
    "TAGS",
    "SOURCE"
]
