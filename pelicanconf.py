AUTHOR = 'Vladimír Vondruš'

#M_SITE_LOGO = 'gr/logo.png'
M_SITE_LOGO_TEXT = 'Magnum'

SITENAME = 'Magnum Engine'
SITESUBTITLE = 'C++11/C++14 and OpenGL graphics engine'
SITEURL = ''

M_BLOG_NAME = 'Magnum Engine Blog'
M_BLOG_URL = 'blog/'

PATH = 'content'
ARTICLE_PATHS = ['blog']

PAGE_PATHS = ['']
PAGE_EXCLUDES = ['doc', 'img']
READERS = {'html': None} # HTML files are only ever included from reST

STATIC_PATHS = ['img', 'showcase']
STATIC_URL = 'static/{path}'
STATIC_SAVE_AS = 'static/{path}'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARCHIVES_URL = 'blog/'
ARCHIVES_SAVE_AS = 'blog/index.html'
ARTICLE_URL = '{slug}/' # blog/category/ is part of the slug
ARTICLE_SAVE_AS = '{slug}/index.html'
DRAFT_URL = '{slug}-draft/'
DRAFT_SAVE_AS = '{slug}-draft/index.html'
AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = 'blog/author/{slug}/index.html'
CATEGORY_URL = 'blog/{slug}/'
CATEGORY_SAVE_AS = 'blog/{slug}/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

AUTHORS_SAVE_AS = None # Not used
CATEGORIES_SAVE_AS = None # Not used
TAGS_SAVE_AS = None # Not used

PAGINATION_PATTERNS = [(1, '{base_name}/', '{base_name}/index.html'),
                       (2, '{base_name}/{number}/', '{base_name}/{number}/index.html')]

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = 'en'

import platform
if platform.system() == 'Windows':
    DATE_FORMATS = {'en': ('usa', '%b %d, %Y')}
else:
    DATE_FORMATS = {'en': ('en_US.UTF-8', '%b %d, %Y')}

FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

M_LINKS_NAVBAR1 = [('Features', 'features/', 'features', [
                        ('Extra Functionality', 'features/extras/', 'features/extras'),
                        ('Plugins & Extensions', 'features/extensions/', 'features/extensions')]),
                   ('Showcase', 'showcase/', 'showcase', []),
                   ('Docs', '//doc.magnum.graphics/', '', [
                        ('Getting Started', '//doc.magnum.graphics/magnum/getting-started.html', ''),
                        ('Corrade', '//doc.magnum.graphics/corrade/', ''),
                        ('Magnum', '//doc.magnum.graphics/magnum/', ''),
                        ('Doc Downloads', 'doc-downloads/', 'doc-downloads')])]

M_LINKS_NAVBAR2 = [('Blog', M_BLOG_URL, '[blog]', []),
                   ('Contact & Support', 'contact/', 'contact', [
                        ('GitHub', 'https://github.com/mosra/magnum', ''),
                        ('About the Project', 'about/', 'about')])]

M_LINKS_FOOTER1 = [('Magnum', '/'),
                   ('Features', 'features/'),
                   ('Extra Functionality', 'features/extras/'),
                   ('Plugins & Extensions', 'features/extensions/'),
                   ('Showcase', 'showcase/'),
                   ('Build Status', 'build-status/')]

M_LINKS_FOOTER2 = [('Docs', '//doc.magnum.graphics/'),
                   ('Getting Started', '//doc.magnum.graphics/magnum/getting-started.html'),
                   ('Corrade', '//doc.magnum.graphics/corrade/'),
                   ('Magnum', '//doc.magnum.graphics/magnum/'),
                   ('Doc Downloads', 'documentation-downloads/')]

M_LINKS_FOOTER3 = [('Contact & Support', 'contact/'),
                   ('About the Project', 'about/'),
                   ('Blog Feed', M_BLOG_URL + '/feeds/all.atom.xml'),
                   ('GitHub', 'https://github.com/mosra/magnum'),
                   ('Gitter', 'https://gitter.im/mosra/magnum'),
                   ('Twitter', 'https://twitter.com/czmosra'),
                   ('Google Groups', 'https://groups.google.com/forum/#!forum/magnum-engine')]

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Code+Pro:400,400i,600%7CSource+Sans+Pro:400,400i,600,600i&subset=latin-ext',
               'static/m-dark.css']

M_FINE_PRINT = """
| Magnum Engine. Copyright © `Vladimír Vondruš <http://mosra.cz>`_ and
  contributors, 2010--2017.
| Site powered by `Pelican <https://getpelican.com>`_ and
  `m.css <http://mcss.mosra.cz>`_. Contact the team via
  `GitHub <https://github.com/mosra/magnum>`_, `Gitter <https://gitter.im/mosra/magnum>`_,
  `e-mail <mailto:magnum-engine@googlegroups.com>`_, or
  `Twitter <https://twitter.com/czmosra>`_.
"""

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['m.css/pelican-plugins']
PLUGINS = ['m.abbr',
           'm.code',
           'm.components',
           'm.dox',
           'm.filesize',
           'm.gh',
           'm.gl',
           'm.htmlsanity',
           'm.images',
           'm.math']

FORMATTED_FIELDS = ['summary', 'description', 'landing', 'header', 'footer']

THEME = 'm.css/pelican-theme/'
THEME_STATIC_DIR = 'static/'

M_THEME_COLOR = '#22272e'
M_SOCIAL_TWITTER_SITE = '@czmosra'
M_SOCIAL_TWITTER_SITE_ID = 1537427036
M_SOCIAL_IMAGE = 'static/site.jpg'

M_HTMLSANITY_SMART_QUOTES = True
M_HTMLSANITY_HYPHENATION = True
M_DOX_TAGFILES = [
    ('content/doc/corrade.tag', 'http://doc.magnum.graphics/corrade/', ['Corrade::']),
    ('content/doc/magnum.tag', 'http://doc.magnum.graphics/magnum/', ['Magnum::'])]
M_IMAGES_REQUIRE_ALT_TEXT = True

DIRECT_TEMPLATES = ['archives']
PAGINATED_DIRECT_TEMPLATES = ['archives']

SLUGIFY_SOURCE = 'basename'
PATH_METADATA = '(?P<slug>.+).rst'
SLUG_SUBSTITUTIONS = [('C++', 'cpp')]
