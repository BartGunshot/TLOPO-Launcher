# TLOPO Launcher for multi-distribution launching.
#
# python 3.7
import APIRequests
import Downloader
import StartGame
import getpass


# TODO: Replace main with a GUI
def get_response(token=False):
    # Input username and password store in data dict
    username = input("Username: ")
    password = getpass.getpass('Password: ')
    # If token requested then get that as well
    if token:
        gtoken = input("2FA Code: ")
        data = {'username': username,
                'password': password,
                'gtoken': gtoken}
    else:
        data = {'username': username,
                'password': password}

    # Create APIRequest object
    requester = APIRequests.APIRequest()
    # Get version (test, dev, live)
    if username.find('@') != -1:
        ver = username[username.find('@')+1:]
    else:
        ver = 'live'

    # Pass username/password dict to the APIRequest
    return requester.get_login_response(data), ver


### GET RESPONSE TO LOGIN
# Login success code = 7
while True:
    response, version = get_response()
    print(response.get('message'))
    if response.get('status') == 7:
        break
    # Status 3 = 2FA
    elif response.get('status') == 3:
        response, version = get_response(token=True)
        # Check to make sure login success
        if response.get('status') == 7:
            break
        else:
            continue
    # Status 11 - Arrmor location verification
    elif response.get('status') == 11:
        print('Please check your email for "Arrmor" Verification.')
        continue
    else:
        continue

### VERIFY FILES/DOWNLOAD
downlder = Downloader.Downloader(version)
downlder.start_download()

### START GAME
StartGame.start_game(response, version)
