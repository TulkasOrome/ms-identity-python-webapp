import os

# Application (client) ID of app registration
CLIENT_ID = os.getenv("efbfa13c-1935-471b-a6e6-dec032d43407")
# Application's generated client secret: never check this into source control!
CLIENT_SECRET = os.getenv("6Pz8Q~ABgeHIv1xj.1D00qU3XNg~FrPGTAQXLbH-")

# You can configure your authority via environment variable
# Defaults to a multi-tenant app in world-wide cloud
AUTHORITY = os.getenv("AUTHORITY", "https://login.microsoftonline.com/common")

REDIRECT_PATH = "/microsoft/auth"  # Used for forming an absolute URL to your redirect URI.
# The absolute URL must match the redirect URI you set
# in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/users'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["User.ReadBasic.All"]

# Tells the Flask-session extension to store sessions in the filesystem
SESSION_TYPE = "filesystem"
# Using the file system will not work in most production systems,
# it's better to use a database-backed session store instead.

CHATWOOT_API_ENDPOINT = "https://hiverhq.co.in/"

CHATWOOT_PLATFORM_APP_API_KEY = "BFjxtpD1m6Q8ups3Rcd9JTVe"

HIVER_API_DB_ENDPOINT = "hiver-sql-awtest.cd1wuzxpxrbp.us-west-2.rds.amazonaws.com:3306"
