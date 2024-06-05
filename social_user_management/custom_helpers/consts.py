from datetime import timedelta
from cryptography.hazmat.primitives import serialization



DEFAULT_ROLE = "local_system"
STATUS_ACTIVE = 1
CREATION_BY = "system"
HTTP_REQUEST_ID = 'local_id'

DATE_FORMAT = "date_format"
TIME_FORMAT = "time_format"

DATE_YYYY_MM_DD = "%Y-%m-%d"
DATE_YYYY_MM_DD_HH_MM_SS = "%Y-%m-%d %H:%M:%S"
DATE_YYYY_MM = "%Y-%m"
TIME_HH_MM_SS = "%H:%M:%S"
DATE_MM_DD_YYYY = "%-m/%d/%Y"
DATE_DD_MM_YYYY = "%d-%m-%Y"
DATE_YYYY = "%Y"

SALTING_CONSTANT = "_user"

ALGORITHM_OF_JWT = 'RS256'
LIFE_TIME_OF_ACCESS_TOKEN = timedelta(minutes=15)
LIFE_TIME_OF_REFRESH_TOKEN = timedelta(days=365)

# The following Private key made through the OS Environment variables
base_dir = r"..\custom_helpers\..\social_user_management\..\Social_Platform\private_key.pem"

with open(base_dir, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
)

JWT_KEY_PRIVATE = private_key
STATUS_CODE = 'status_code'
SUCCESS_CODE = 10000
MESSAGE = 'message'

COMMON_CHECK_FORMAT_TYPE = {
        DATE_FORMAT: 10,
        TIME_FORMAT: 11
}

gender_dict = {
    "male": 1,
    "female": 2
}

friend_acceptance_state = {
    "pending": 0,
    "accepted": 1,
    "rejected": 2
}

