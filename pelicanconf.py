AUTHOR = 'KKM'
SITENAME = 'Kinderkleidermarkt St. Peter'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Flohmarkthelfer (Verkäufer-Portal)', 'https://kinderkleidermarkt-st-peter.flohmarkthelfer.de/'),
    ('Mitteilungsblatt der Gemeinde St. Peter', 'http://st-peter.eu/amtliches-mitteilungsblatt.html'),)

THEME = './themes/pelican-blue'

FAVICON = '/images/favicon.ico'

AVATAR = '/images/kkm-logo-freigestellt-gelb.png'


# Social widget
#SOCIAL = (
#    ("You can add links in your config file", "#"),
#    ("Another social link", "#"),
#)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

DISPLAY_SUMMARY = True

MENUITEMS = (('Start', SITEURL),)

DISPLAY_CATEGORIES_ON_MENU = False

