# TLOPO Launcher for multi-distribution launching.
# Handle requests to the API
#

import requests
from launcherglobals import API_URLS, HEADERS


class APIRequester:
    """APIRequest handles all requests to the TLOPO API."""

    # Login

    def get_login_response(self, userdata):
        return requests.post(API_URLS.get('login'), data=userdata, headers=HEADERS).json()

    # Blog Posts and News requests

    def get_launcher_news(self):
        """Returns a pre-formatted HTML document for use within the launcher."""
        return requests.get(API_URLS.get('launcher_news'))

    def get_feed_news(self, num=5):
        """Returns a JSON object containing the requested number of blog posts and their information."""
        return requests.get(API_URLS.get('feed_news') + str(num))

    def get_release_notes(self, num=5):
        """Returns a JSON object containing requested number of release notes and their information"""
        return requests.get(API_URLS.get('release_notes') + str(num))

    def get_notification_banner(self):
        """Returns a JSON object with the currently active banner."""
        return requests.get(API_URLS.get('notification_banner'))

    # Gameserver requests

    def get_oceans(self):
        """Returns a JSON object with all information of current oceans."""
        return requests.get(API_URLS.get('oceans'))

    # System Status and Services

    def get_online_status(self):
        """Returns a JSON object containing the statues of TLOPO system services."""
        return requests.get(API_URLS.get('online_status'))
