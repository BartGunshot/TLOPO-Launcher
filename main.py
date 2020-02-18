# TLOPO Launcher for multi-distribution launching.
#
#
import APIRequests
import Downloader
import StartGame


# TODO: Replace main with a GUI
def getReponse(token=False):
    # Input username and password store in data dict
    username = input("Username: ")
    password = input("Password: ")
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
    return requester.getLoginResponse(data), ver


### GET RESPONSE TO LOGIN
# Login success code = 7
while True:
    response, version = getReponse()
    print(response.get('message'))
    if response.get('status') == 7:
        break
    # Status 3 = 2FA
    elif response.get('status') == 3:
        response, version = getReponse(token=True)
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
downlder.startDownload()

### START GAME
StartGame.startGame(response, version)
