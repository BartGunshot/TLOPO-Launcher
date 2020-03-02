# TLOPO Launcher for multi-distribution launching.
# Module for storing globals: API urls, file paths, etc.
#

API_URLS = {
    'login': 'https://api.tlopo.com/login/',
    'launcher_news': 'https://api.tlopo.com/launcher/',
    'feed_news': 'https://api.tlopo.com/news/feed/',
    'release_notes': 'https://api.tlopo.com/releases/feed/',
    'notification_banner': 'https://api.tlopo.com/news/notification',
    'oceans': 'https://api.tlopo.com/shards/',
    'online_status': 'https://api.tlopo.com/system/status'
}

API_DOWNLOAD = {
    'server-live': 'https://download.tlopo.com/',
    'server-test': 'https://download-test.tlopo.com/',
    'server-dev': 'https://download-dev.tlopo.com/',
    'win32': 'win32/',
    'win64': 'win64/',
    'linux2': 'linux2/',
    'linux': 'linux2/',
    'darwin': 'mac/',
    'patcher': 'patcher.json',
    'patches': 'patches/'
}

# TODO: Make non-windows specific
FILEPATHS = {
    'default': '\\Program Files (x86)\\TLOPO',
    'test': '\\TEST',
    'live': '\\LIVE',
    'dev': '\\dev'
}

EXECUTABLES = {
    'live': 'tlopo',
    'test': 'tlopo_test',
    'dev': 'tlopo_dev'
}

HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
