# TLOPO Launcher for multi-distribution launching.
# Starts the game
#
import os
from launcherglobals import FILEPATHS, EXECUTABLES


def start_game(response, distr):
    # Set OS environ variables for gameserver and playcookie
    os.environ['TLOPO_GAMESERVER'] = response.get('gameserver')
    os.environ['TLOPO_PLAYCOOKIE'] = response.get('token')

    # Set up file and paths for distributions
    if distr == 'live':
        location = FILEPATHS.get('live')
        exe = EXECUTABLES.get('live')
    elif distr == 'test':
        location = FILEPATHS.get('test')
        exe = EXECUTABLES.get('test')
    elif distr == 'dev':
        location = FILEPATHS.get('dev')
        exe = EXECUTABLES.get('dev')

    # TODO: Make path and executables non-windows specific as possible
    os.chdir(os.getcwd() + location)
    os.system(exe + '.exe')
