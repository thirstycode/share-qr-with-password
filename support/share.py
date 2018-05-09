import sys
import dropbox

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
from dropbox.sharing import CreateSharedLinkArg
from config import TOKEN

def backup(dbx,LOCALFILE,BACKUPPATH):
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
            result  = dbx.sharing_create_shared_link_with_settings(path = BACKUPPATH)
            return result.url
        except ApiError as err:
            # This checks for the specific error where a user doesn't have enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()



# Run this script independently
def upload(LOCALFILE,BACKUPPATH):
    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. Open up backup-and-restore-example.py in a text editor and paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit(
            "ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

    # print("Creating backup...")
    # Create a backup of the current settings file
    url = backup(dbx,LOCALFILE,BACKUPPATH)
    return url
