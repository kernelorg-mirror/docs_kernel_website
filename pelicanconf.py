#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
import os
import sys
sys.path.append('./')
from plugins import releases  # noqa

SITENAME = 'The Linux Kernel Archives'
SITEURL = 'https://www.kernel.org'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

DATE_FORMATS = {
        'en': '%Y-%m-%d',
    }

DEFAULT_DATE = 'fs'
FILENAME_METADATA = r'.*(?P<date>\d{4}-\d{2}-\d{2}).*'

# ARTICLE_URL = u'posts/{date:%Y}-{date:%m}-{date:%d}/{slug}.html'
# ARTICLE_SAVE_AS = u'posts/{date:%Y}-{date:%m}-{date:%d}/{slug}.html'

# Dirs to always push to site
STATIC_PATHS = (['files', 'corporate', 'images', 'news/images'])

# NB: Don't add a kernel to longterm if it's the only stable kernel currently
#     listed on www.kernel.org. This will break people's scripts, so we don't
#     support doing it. Wait till there's an x.x.1 of the next stable branch.
LONGTERM_KERNELS = ('6.18', '6.12', '6.6', '6.1', '5.15', '5.10', '5.4',
                    '4.19', '4.14', '4.9', '4.4', '4.1', '3.18', '3.10', '3.2')

EOL_KERNELS = ('3.2', '3.4', '3.10', '3.12', '3.14', '3.16', '3.18', '3.19',
               '4.0', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8',
               '4.9', '4.10', '4.11', '4.12', '4.13', '4.14', '4.15', '4.16', '4.17',
               '4.18', '4.19', '4.20', '5.0', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6',
               '5.7', '5.8', '5.9', '5.11', '5.12', '5.13', '5.14', '5.16',
               '5.17', '5.18', '5.19', '6.0', '6.2', '6.3', '6.4', '6.5', '6.7',
               '6.8', '6.9', '6.10', '6.11', '6.13', '6.14', '6.15', '6.16', '6.17')

# Continuity for major version jumps
# maj_rel: prev_mainline
MAJOR_JUMPS = {
               '3': '2.6.39',
               '4': '3.19',
               '5': '4.20',
               '6': '5.19',
               '7': '6.19',
              }

if 'GIT_REPOS' in os.environ.keys():
    GIT_REPOS = os.environ['GIT_REPOS']
else:
    GIT_REPOS = '/mnt/git-repos/repos'

if 'PELICAN_STATEDIR' in os.environ.keys():
    PELICAN_STATEDIR = os.environ['PELICAN_STATEDIR']
else:
    PELICAN_STATEDIR = '/var/lib/mirror'

GIT_MAINLINE = os.path.join(GIT_REPOS, 'pub/scm/linux/kernel/git/torvalds/linux.git')
GIT_STABLE = os.path.join(GIT_REPOS, 'pub/scm/linux/kernel/git/stable/linux.git')
GIT_NEXT = os.path.join(GIT_REPOS, 'pub/scm/linux/kernel/git/next/linux-next.git')

RELEASE_TRACKER = os.path.join(PELICAN_STATEDIR, 'release-tracker.json')

PLUGINS = [releases]

# Blogroll
LINKS = (
    ('Git Trees', 'https://git.kernel.org/'),
    ('Documentation', 'https://docs.kernel.org/'),
    ('Kernel Mailing Lists', 'https://lore.kernel.org/'),
    ('Patchwork', 'https://patchwork.kernel.org/'),
    ('Wikis', 'https://www.wiki.kernel.org/'),
    ('Bugzilla', 'https://bugzilla.kernel.org/'),
    ('Mirrors', 'https://mirrors.kernel.org/'),
    ('Linux.com', 'https://www.linux.com/'),
    ('Linux Foundation', 'https://www.linuxfoundation.org/'),
)

# Social widget
SOCIAL = (
    ('Kernel Planet', 'https://planet.kernel.org/'),
)

THEME = './korgi'
DEFAULT_PAGINATION = 10
