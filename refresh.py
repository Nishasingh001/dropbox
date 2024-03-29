import dropbox
from dropbox.oauth import DropboxOAuth2FlowNoRedirect

# Your app key and secret


APP_KEY = "4ns2gt309k2kftk"
APP_SECRET = "viigzulo2py11mz"

TOKEN = "sl.Bw4TuGoxWvNcMrIZ_wiTEqGh0XJeZt5z32iUzaVLoc9xlSttdSjHRmPOSYKS8T3X24HBDXPkYjYwdGSEPAjtQxemjJC4EGp0jbeYnKeOXyrdRwb8TqH-ItQsq3yDPNneOthxbCQ1wxuUo3xD-bvgoVA"

import dropbox

# Dropbox app key and secret obtained from the Dropbox App Console

# Initialize Dropbox OAuth2 flow
auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

# Get authorization URL
authorize_url = auth_flow.start()

# Direct the user to the authorization URL
print("1. Go to: " + authorize_url)
print("2. Click 'Allow' (you might have to log in first)")
print("3. Copy the authorization code.")

# Handle the authorization code
authorization_code = input("Enter the authorization code here: ")

# Exchange authorization code for access and refresh tokens
try:
    oauth2_result = auth_flow.finish(authorization_code)
    access_token = oauth2_result.access_token
    refresh_token = oauth2_result.refresh_token
    print("Access token:", access_token)
    print("Refresh token:", refresh_token)
except Exception as e:
    print("Error:", e)
