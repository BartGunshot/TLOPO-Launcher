# TLOPO Launcher for multi-distribution launching.
#
# python 3.7
import apirequests
import settings
import downloader
import startgame
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
    requester = apirequests.APIRequester()
    # Get version (test, dev, live)
    if username.find('@') != -1:
        ver = username[username.find('@')+1:]
    else:
        ver = 'live'

    # Pass username/password dict to the APIRequest
    return requester.get_login_response(data), ver

def doLogin():
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
    downlder = downloader.Downloader(version)
    downlder.start_download()

    ### START GAME
    startgame.start_game(response, version)

def editSettings(ver):
    s = settings.Settings(ver)
    for key, value in s.read().items():
        print(key + ': ' + value)
    while True:
        print("Enter entry to modify or type q to quit.")
        choice = input(">>> ")
        if choice == 'q':
            break;
        elif choice in s.settingsdict.keys():
            value = input(choice + ">>>")
            s.settingsdict[choice] = value
        else:
            print("Invalid selection.\n")
    s.write()

def doSettings():
    while True:
        print("Settings Menu\n-------------")
        print("   1. Edit live settings")
        print("   2. Edit test settings")
        print("   3. Edit dev settings")
        print("   4. Exit Settings")
        choice = input(">>> ")
        if choice == "1":
            editSettings('live')
        elif choice == "2":
            editSettings('test')
        elif choice == "3":
            editSettings('dev')
        elif choice == "q" or choice == "4":
            break;
        else:
            print("Invalid selection.\n\n")

### GET RESPONSE TO LOGIN
# Login success code = 7
while True:
    print("MENU\n------------")
    print("  1. Login")
    print("  2. Settings")
    print("  3. Quit")
    choice = input(">>> ")
    if choice == "1":
        doLogin()
    elif choice == "2":
        doSettings()
    elif choice == "3" or choice == "q":
        break;
    else:
        print("Invalid selection.\n\n")


