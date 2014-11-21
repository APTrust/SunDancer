# API ADMIN account token for your local api server.
API_KEY = ""
# local API server root url
API_URL = "" # 'http://localhost:8000'
# My own node namespace
NAMESPACE = "aptrust"

# The number of nodes to copy with
NODE_COPIES = 2

# Domain name fo the server to use in rsync
STAGING_SERVER = '' # 'devops.aptrust.org'

# Absolute Path to the directory holding the files for replication
STAGING_DIR = '' # '/home/aptrustdpn/files/staging'

# DateFormat used for DPN Datetime strings.
DPN_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

# Information about directories to use for staging content to nodes.
NODE_DIRS = {
    'chron': {
        'USERNAME': 'dpn.chron',
        'CONTENT_DIR': '',
        'CONTENT_PATH': 'outbound/',
    },
    'tdr': {
        'USERNAME': 'dpn.tdr',
        'CONTENT_DIR': '',
        'CONTENT_PATH': 'outbound/',
    }
}
