# TLOPO Launcher for multi-distribution launching.
# Handle downloads and file updating/patching for TLOPO
#
import os
import requests
import pathlib
from bz2 import BZ2Decompressor
from hashlib import sha256
from sys import platform
from launcherglobals import API_DOWNLOAD, FILEPATHS


# TODO: This needs major cleanup
class Downloader:
    """Downloader handles making sure files are up-to-date."""

    def __init__(self, distr):
        self.system = platform
        self.currdir = pathlib.Path.cwd()

        # Test server changed win32 path to win64
        if self.system == 'win32' and distr != 'live':
            self.system = 'win64'

        # Get distribution's download server
        if distr == 'live':
            self.server = API_DOWNLOAD.get('server-live')
            self.location = pathlib.Path(FILEPATHS.get('live'))
        elif distr == 'test':
            self.server = API_DOWNLOAD.get('server-test')
            self.location = pathlib.Path(FILEPATHS.get('test'))
        elif distr == 'dev':
            self.server = API_DOWNLOAD.get('server-dev')
            self.location = pathlib.Path(FILEPATHS.get('dev'))

        self.downloadServer = self.server + API_DOWNLOAD.get(self.system)
        self.manifest = self._get_patch_manifest()

    def _get_patch_manifest(self):
        return requests.get(self.downloadServer + API_DOWNLOAD.get('patcher')).json()

    def start_download(self):
        # Iterate through patch manifest
        for filename in self.manifest.get('files'):
            file = pathlib.Path(self.currdir, self.location, filename)
            if file.exists():

                # If file exists then open it and compare SHA256 hash first 7 chars
                # TODO: Move this into sub function for less clutter
                with open(file, 'rb') as existingfile:

                    binary = existingfile.read()
                    # TODO: This sub-dict accessing can probably be cleaned up
                    if self.manifest.get('files').get(filename).get('hash') != sha256(binary).hexdigest()[:7]:
                        # TODO: Check for patches from manifest and apply them.
                        self._download(filename)
            else:
                # If file dne download it
                self._download(filename)

    def _download(self, filename):
        # GET request from TLOPO download servers for file, all files are downloaded w/ .b2 extension
        data = requests.get(self.downloadServer + filename + '.bz2', stream=True)
        file = pathlib.Path(self.currdir, self.location, filename)

        # If file path does not exist create it
        if not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))

        # Write file from downloaded content, decompress bz2 directly from memory before writing
        decompressor = BZ2Decompressor()
        with open(file, 'wb') as content:
            for chunk in data.iter_content(chunk_size=128):
                content.write(decompressor.decompress(chunk))


    def _download_patches(self):
        pass

    def _check_hash(self):
        pass

